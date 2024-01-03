from django import forms

from .models import Product


class CreateProductForm(forms.ModelForm):
    ids = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Enter IDs separated by comma.", "class": "form-control"}
        )
    )

    class Meta:
        model = Product
        fields = ["ids"]
