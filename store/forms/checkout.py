from django import forms


PAYMENT = (
    ("C", "Готівкова"),
    ("B", "Безготівкова"),
)

class CheckoutForm(forms.Form):
    zip = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT)
