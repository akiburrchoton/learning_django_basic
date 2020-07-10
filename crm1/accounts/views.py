from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    allOrders       = Order.objects.all()
    allCustomers    = Customer.objects.all()
    
    totalCustomers  = allCustomers.count()
    totalOrders     = allOrders.count()
    
    delivered       = allOrders.filter(status="Delivered").count()
    pending         = allOrders.filter(status="Pending").count()


    context = {
        'orders': allOrders, 
        'customers': allCustomers, 'total_customers': totalCustomers,
        'total_orders': totalOrders, 
        'delivered': delivered, 
        'pending': pending
    }
    
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    allProducts = Product.objects.all()

    context     = {
        'products' : allProducts
    }

    return render(request, 'accounts/products.html', context)
    
def customer(request, pk_test):
    customerBasedOnId = Customer.objects.get(id=pk_test)
    ordersByCustomer  = customerBasedOnId.order_set.all()
    numberOfOrders    = ordersByCustomer.count()
    context = {
        'customer'      : customerBasedOnId,
        'orders'        : ordersByCustomer,
        'number_count'  : numberOfOrders
    }

    return render(request, 'accounts/customer.html', context)