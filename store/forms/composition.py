from django import forms
from store.models.composition import CreateComposition


class CreateCompositionForm(forms.ModelForm):
    class Meta:
        model = CreateComposition
        fields = "__all__"
        widgets = {
            'fruit': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'candies': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'vegitables': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'cheese': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'sausages': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'alcohol': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'snacks': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'cones': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'needles': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'christmas_decorations': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'joke_decorations': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'handmade_decorations': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'flowers': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
            'fake_flowers': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;'}),
        }
