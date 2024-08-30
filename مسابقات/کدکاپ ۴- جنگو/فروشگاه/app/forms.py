from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data['price']
        if price > 1000:
            message = 'Product is too expensive'
            raise forms.ValidationError(message)
        return price

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) <= 20:
            message = 'Product must have a good description'
            raise forms.ValidationError(message)
        return description
