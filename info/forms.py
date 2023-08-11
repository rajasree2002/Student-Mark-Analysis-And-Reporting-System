from django import forms
from .models import ContactMessage
from .models import Email

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class Email(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['subject', 'message', "recipient_list", 'sent']
