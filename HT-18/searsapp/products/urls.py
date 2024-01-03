from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.MyProductsView.as_view(), name="my_products"),
    path("product/<int:pk>/", views.ProductView.as_view(), name="product_details"),
    path("product/add/", views.ProductCreateView.as_view(), name="add_product"),
]
