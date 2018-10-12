from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(
                            required=False,
                            widget=forms.Textarea(
                                attrs={

                                    "class": "hello",
                                    "id": "hello_id",
                                    "rows": 5
                                }
                            ))
    price = forms.DecimalField(initial=19.9)
