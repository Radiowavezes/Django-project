from django.contrib.auth.models import User
from django import forms
from .models import Feedback, Callback
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'email',
            'first_name', 
            'last_name'
        ]
        
class ContactForm(forms.Form):
    class Meta:
        model = Feedback
        fields = [
            'full_name', 
            'sender', 
            'phone', 
            'message', 
        ]

class CallbackForm(forms.Form):
    class Meta:
        model = Callback
        fields = '__all__'
