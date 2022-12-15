from django import forms
from .models import CreateComposition

PAYMENT = (
    ('C', 'Готівкова'),
    ('B', 'Безготівкова')
)

class CheckoutForm(forms.Form):
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, 
        choices=PAYMENT
        )


class CreateCompositionForm(forms.ModelForm):
    class Meta:
        model = CreateComposition
        fields = '__all__'
