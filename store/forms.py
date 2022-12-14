from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT = (
    ('C', 'Готівкова'),
    ('B', 'Безготівкова')
)

class CheckoutForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+380'
    }))
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
    widget=forms.RadioSelect, choices=PAYMENT)