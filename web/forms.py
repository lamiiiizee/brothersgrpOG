from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput
from django.forms.widgets import NumberInput
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            # 'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your E-mail'}),
            'number': NumberInput(attrs={'class': 'form-control no-spin', 'placeholder': 'Your Phone Number'}),
            # 'website': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Website'}),
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Services'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }
