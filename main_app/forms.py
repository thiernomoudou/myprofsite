from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-element'}), help_text='Your Name')
    email = forms.EmailField( widget=forms.TextInput(attrs={'class': 'form-control form-element'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-element'}))
