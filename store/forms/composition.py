from django import forms
from store.models.composition import CreateComposition


class CreateCompositionForm(forms.ModelForm):
    class Meta:
        model = CreateComposition
        fields = "__all__"
