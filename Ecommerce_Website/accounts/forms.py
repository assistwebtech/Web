from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.forms import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Address


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


# class AadharCard(forms.ModelFrom):
#     # aadharcard_name = forms.CharField(max_length=30, required=False, help_text='Optional')
#     # aadharcard_number = forms.CharField(max_length=30, required=False, help_text='Optional')
#     class Meta:
#         model = Profile
#         fields = ('aadharcard_name', 'aadharcard_number')
#
#
# class PanCard(forms.ModelFrom):
#     # pancard_name = forms.CharField(max_length=30, required=False, help_text='Optional')
#     # pancard_number = forms.CharField(max_length=30, required=False, help_text='Optional')
#     class Meta:
#         model = Profile
#         fields = ('pancard_name', 'pancard_number')