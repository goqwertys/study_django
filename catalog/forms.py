from django import forms
from django.forms import BooleanField
from prompt_toolkit.validation import ValidationError

from .models import Product
from PIL import Image


forbidden_words = [
    'казино',
    'биржа',
    'обман',
    'криптовалюта',
    'дешево',
    'полиция',
    'крипта',
    'бесплатно',
    'радар'
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'pic', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter product name'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Enter a description',
            'rows': 4
        })
        self.fields['pic'].widget.attrs.update({
            'accept': 'image/*',
            'id': 'custom_id_pic'
        })
        self.fields['price'].widget.attrs.update({
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

    def clean_pic(self):
        pic = self.cleaned_data.get('pic')
        if pic:
            if not pic.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise forms.ValidationError('Unsupported file format')

            if pic.size > 5 * 1024 * 1024:
                raise forms.ValidationError('File size exceeds the limit of 5 MB.')

            try:
                with Image.open(pic) as img:
                    img.verify()
            except Exception:
                raise ValidationError('Invalid image file.')

        return pic
