from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    department = forms.CharField(
        label='Departamento',
        widget=forms.Select(choices=ShippingAddress.DEPARTMENT_CHOICES, attrs={'class': 'form-control'})
    )

    municipality = forms.CharField(
        label='Municipio',
        widget=forms.Select(choices=[], attrs={'class': 'form-control'})
    )

    class Meta:
        model = ShippingAddress
        fields = [
             'street_type', 'line1', 'line2', 'line3', 'department', 'municipality', 'postal_code', 'is_home_or_work', 'reference'
        ]
        labels = {
            'is_home_or_work': 'Es casa o trabajo',
            'street_type': 'tipo de calle',
            'line1': 'Avenida',
            'line2': 'Número',
            'line3': '',
            'postal_code': 'Codigo Postal',
            'reference': 'Referencia',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['department'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['municipality'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['street_type'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['line1'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['line2'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['line3'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['postal_code'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '0000'
        })

        self.fields['is_home_or_work'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['reference'].widget.attrs.update({
            'class': 'form-control'
        })
