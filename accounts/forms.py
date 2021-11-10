from django import forms
from .models import Account

# Based on The Code Institute Boutique Ado project Profile App - Part 5

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '*******',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '*******',
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'John'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Smith'
        self.fields['phone_number'].widget.attrs['placeholder'] = '077421 65890'
        self.fields['email'].widget.attrs['placeholder'] = 'john.smith@example.com'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'