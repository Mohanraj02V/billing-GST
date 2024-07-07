from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customers,Products


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    


class CreateProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    Business = forms.CharField(max_length=100)
    adress = forms.CharField(max_length=255)
    Email = forms.EmailField()
    phonenumber = forms.CharField(max_length=15)
    GST = forms.CharField(max_length=15)
  
from django import forms

class gstForm(forms.Form):
    storeName =forms.CharField(label='Store Name')
    storePhone=forms.IntegerField(label='Store Phone')
    ProductName=forms.CharField(max_length=100)
    Quantity=forms.IntegerField(label='Quantity')
    OrginalAmount = forms.IntegerField(label='OrginalAmount')
    GST = forms.IntegerField(label='GST')

    customerName =forms.CharField(label='Customer Name')
    customerPhone =forms.IntegerField(label='Customer Phone')
   
class customerForm(forms.ModelForm):
    class Meta:
        model =customers
        fields =['CustomerName','CustomerAddress','CustomerMobileNumber','CustomerGST']
        
class productForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =['product_name','product_quantity','product_price','product_discount','product_gst']           