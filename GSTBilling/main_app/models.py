from django.db import models


# Create your models here.



class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
    product_discount = models.IntegerField()
    product_gst = models.IntegerField()
    
    def __str__(self) -> str:
       return f"{self.product_name} => {self.product_quantity} => {self.product_price} =>{self.product_discount} =>{self.product_gst}"

class Meta:
    db_table ="Products"


# class Profiles(models.Model):
#     name =models.CharField(max_length=40)
#     lastname=models.CharField(max_length=40)
#     Business=models.CharField(max_length=100)
#     adress=models.CharField(max_length=200)
#     Email=models.EmailField()
#     phonenumber=models.BigIntegerField()
#     GST=models.CharField(max_length=15)

# class Meta:
#     alldetails_table ='Profiles'

from django.db import models

class Profiles(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Business = models.CharField(max_length=100)
    adress = models.CharField(max_length=255)
    Email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    GST = models.CharField(max_length=15)
class Meta:
     alldetails_table ="Profiles"
        
    
class customers(models.Model):
    CustomerName =models.CharField(max_length=100)
    CustomerAddress=models.CharField(max_length=200)  
    CustomerMobileNumber=models.BigIntegerField()
    CustomerGST=models.CharField(max_length=15)
    

    def __str__(self) -> str:
       return f"{self.CustomerName} => {self.CustomerAddress} => {self.CustomerMobileNumber} =>{self.CustomerGST}"
    
class Meta:
     alldetails_table ="customers"
     
class gstResults(models.Model):
    storeName =models.CharField(max_length=100)
    storePhone=models.BigIntegerField()
    ProductName=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    OrginalAmount = models.IntegerField()
    # number2 = models.IntegerField()
    GST = models.DecimalField(max_digits=5, decimal_places=2)
    Quantity=models.IntegerField()
    
    Total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    customerName =models.CharField(max_length=100)
    customerPhone =models.BigIntegerField()
    
    
    class Meta:
        db_table = "gstResults"    
        
        



