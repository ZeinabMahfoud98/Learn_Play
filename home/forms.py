from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message.', 'rows': 5}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'message': 'Message',
        }
        error_messages = {
            'first_name': {'required': "Please enter your first name."},
            'last_name': {'required': "Please enter your last name."},
            'email': {'required': "Please enter your email address."},
            'message': {'required': "Please write your message."},
        }
