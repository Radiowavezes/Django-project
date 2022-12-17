from django import forms
from posy.models.feedback import Feedback


class ContactForm(forms.Form):
    class Meta:
        model = Feedback
        fields = [
            "full_name",
            "sender",
            "phone",
            "message",
        ]
