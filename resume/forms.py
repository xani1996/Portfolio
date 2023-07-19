from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'contact__inputs'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'contact__inputs'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact__inputs'}))
