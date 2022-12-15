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

class CreateCompositionFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateCompositionFormMixin, self).__init__(*args, **kwargs)
        self.user = kwargs.pop('user')

    def save(self, commit=True):
        object = super(CreateCompositionFormMixin, self).save(commit=False)
        object.user = self.user
        if commit:
            return object.save()
        else:
            return object


class CreateCompositionForm(forms.ModelForm):
    class Meta:
        model = CreateComposition
        fields = '__all__'
