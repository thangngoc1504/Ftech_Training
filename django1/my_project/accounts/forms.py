from django import forms
from django.contrib.auth.models import User
import re


class SignForm(forms.ModelForm):
    password= forms.CharField(label='Password',widget=forms.PasswordInput)
    password2= forms.CharField(label='Repeat Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email','image']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Trùng password")
        return cd['password2']

class EditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','image']