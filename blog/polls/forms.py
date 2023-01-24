from django import forms
from .models import Contact, Coment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = "__all__"