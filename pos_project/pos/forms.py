from django import forms
from .models import Customer


class CustomerInfoForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    first_name = forms.CharField(label='First Name', max_length=20, required=False)
    last_name = forms.CharField(label='Last Name', max_length=20, required=False)
    address_1 = forms.CharField(label='Address', max_length=30, required=False)
    address_2 = forms.CharField(label='Address 2', max_length=30, required=False)
    zip_code = forms.CharField(label='Zip Code', max_length=5, required=False)
    city = forms.CharField(label='City', max_length=20, required=False)

    class Meta:
        model = Customer
        fields = ['phone_number']
