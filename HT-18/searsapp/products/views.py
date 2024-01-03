from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View, generic

from .forms import CreateProductForm
from .models import Product
from .services import is_valid_ids, save_scraped_products


class MyProductsView(generic.ListView):
    template_name = "products/my_products.html"
    context_object_name = "my_products"

    def get_queryset(self):
        return Product.objects.order_by("-pk")


class ProductView(generic.DetailView):
    model = Product
    template_name = "products/product_details.html"


class ProductCreateView(View):
    template_name = "products/add_products.html"
    form_class = CreateProductForm
    success_url = reverse_lazy("products:add_product")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Get ID from form
            form_ids = form.cleaned_data["ids"]

            # Check if valid form input
            if not is_valid_ids(ids=form_ids):
                messages.error(
                    self.request,
                    "Wrong input formatting. Enter IDs separated by comma. "
                    "Example: A098254049,A085642481",
                )
                return HttpResponseRedirect(reverse("products:add_product"))

            product_ids = form.cleaned_data["ids"].split(",")

            # Save all products from ids
            save_scraped_products(product_ids=product_ids)
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {"form": form})
