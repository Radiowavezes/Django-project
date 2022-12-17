from django import forms
from posy.models.callback import Callback


class CallbackForm(forms.Form):
    class Meta:
        model = Callback
        fields = "__all__"
