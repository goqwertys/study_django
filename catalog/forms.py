from django import forms
from .models import Product

forbidden_words = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'pic', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter product name'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter a description',
            'rows': 4
        })
        self.fields['pic'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*',
            'id': 'custom_id_pic'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter product price'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError(f'The word "{word}" is not allowed in the name')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError(f'The word "{word}" is not allowed in the description')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Please enter a price greater than zero')
        return price
