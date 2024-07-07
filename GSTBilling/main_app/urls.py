from django.urls import path
from . import views
from .views import delete
from .views import Customer_delete


urlpatterns = [
    path('home', views.index, name='home'),
    path('login', views.log_in, name='login'),
    path('signup', views.sign_up, name='signup'),
    path('logout', views.log_out, name='logout'),
    path('',views.first, name="first"),
    path('invoice',views.invoice, name='invoice_list'),
    path('createInvoice',views.sum_view, name='create_invoice'),
    path('product',views.product_index, name='product_index'),
    path('productDetails',views.product, name='productDetails'),
    # path('visitProfile',views.visit_Profile,name='visitProfile'),
    # path('createProfile',views.create_profile,name='createProfile'),
    path('cdetails',views.customer_details, name='cdetails'),
    path('customersDatas',views.customers_Datas,name='customersDatas'),
    path('main',views.main,name='createProfile'),
    path('delete/<int:id>/', delete, name='delete_product'),
    path('Customer_delete/<int:id>/', Customer_delete, name='Customer_delete'),
    
    
    path('gstNewsUpdates',views.gstNewsUpdates,name='gstNewsUpdates'),
    path('user',views.todos_for_user,name="user")

   
    
]