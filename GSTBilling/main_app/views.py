from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.contrib import messages
from .models import Products, Profiles, customers, gstResults
from .forms import CreateProfileForm, productForm, customerForm, gstForm
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def todos_for_user(request):
    todos = Products.objects.filter(user=request.user)
    # Return the filtered todos to the user





####### Home Page Url #######
def index(request):
    return render(request, 'index.html')



######## First Page ######
def first(request):
    return render(request,'firstpage.html')


########  View_List Url #######
def view(request):
    return render(request,'view_list.html')

######## Main page ##########

def main(request):
    return render(request,'createProfile.html')





                                    ####### Login SignUp And Logout Code Section ######
                                    
                                    

                                               ####### signup page #######
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



                                             ###### login page #######
                                             
                                             
                                             
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')    
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
           error_message = 'Invalid username or password'
           return render(request, 'login_error.html', {'error_message': error_message})

    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


   
                                             ####### logout page ########
                                             
def log_out(request):
    logout(request)
    return redirect('login')





                                                 #### Product Code Section ######
                                                 


def product(request):
    if request.method == 'POST':
        form=productForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get('product_name')
            product_quantity = form.cleaned_data.get('product_quantity')
            product_price = form.cleaned_data.get('product_price')
            product_discount = form.cleaned_data.get('product_discount')
            product_gst = form.cleaned_data.get('product_gst')
   
        if form.is_valid():
                form.save()    
                return redirect('product_index')
    else:
        form = productForm()
    return redirect('product_index')    
    
def product_index(request):
    key =Products.objects.all()
    return render(request,'product.html',{'data':key})

def delete(request,id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return redirect('product_index')




   
   
  
    
                                   ######## Customer Cose Goes Section ########
                                   


def customers_Datas(request):
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            # customer_mobile_number = form.cleaned_data.get('CustomerMobileNumber')
            CustomerName =form.cleaned_data.get('CustomerName')
            CustomerAddress=form.cleaned_data.get('CustomerAddress')  
            CustomerMobileNumber=form.cleaned_data.get('CustomerMobileNumber')
            CustomerGST=form.cleaned_data.get('CustomerGST')
           
            
        if form.is_valid():
                form.save()
                return redirect('cdetails')
                # return render(request,'customer.html')
            
    else:
        form = customerForm()
    # return redirect(request, 'customer.html', {'form': form})
    return redirect('cdetails')

def customer_details(request):
    fetch=customers.objects.all()
    
    return render(request,'customer.html',{'c_details':fetch})


def Customer_delete(request,id):
    customer = get_object_or_404(customers, id=id)
    customer.delete()
    return redirect('cdetails')
    # return render(request,'customer.html')




                                       ####### GST Calculation Code Section ########
                                       
                                       

def sum_view(request):
    if request.method == 'POST':
        form = gstForm(request.POST)
        if form.is_valid():
            storeName =form.cleaned_data.get('storeName')
            storePhone=form.cleaned_data.get('storePhone')
            ProductName=form.cleaned_data['ProductName']
            Quantity=form.cleaned_data['Quantity']
            OrginalAmount = form.cleaned_data['OrginalAmount']
            GST = form.cleaned_data['GST']

            customerName =form.cleaned_data.get('customerName')
            customerPhone =form.cleaned_data.get('customerPhone')
  
            amount=(OrginalAmount*GST)/100
            Total=OrginalAmount+amount
            gstResults.objects.create(ProductName=ProductName,Quantity=Quantity,OrginalAmount=OrginalAmount, GST=GST, Total=Total,storeName=storeName,storePhone=storePhone,customerName=customerName,customerPhone=customerPhone)
            return redirect('create_invoice')
           
    else:
        form = gstForm()
    return render(request, 'create_invoice.html', {'form': form})

def invoice(request):
    invoiceDetails=gstResults.objects.all()
    return render(request,'invoice.html',{'invoiceDetails':invoiceDetails})




                               ######## Site Details Code Goes Here #######



def gstNewsUpdates(request):
    return render(request,'gstNewsUpdates.html')














