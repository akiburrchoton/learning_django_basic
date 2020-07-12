from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .filters import OrderFilter
from django.forms import inlineformset_factory # formset - multiple forms in a single form
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
    customerBasedOnId   = Customer.objects.get(id=pk_test)
    ordersByCustomer    = customerBasedOnId.order_set.all()
    numberOfOrders      = ordersByCustomer.count()

    myFilter            = OrderFilter(request.GET, queryset=ordersByCustomer)
    ordersByCustomer    = myFilter.qs

    # Context
    context = {
        'customer'      : customerBasedOnId,
        'orders'        : ordersByCustomer,
        'order_count'   : numberOfOrders,
        'showMyFilter'  : myFilter,
    }

    return render(request, 'accounts/customer.html', context)

def createOrder(request, pk):
    OrderFormSet        = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customerBasedOnId   = Customer.objects.get(id=pk)
    
    formset             = OrderFormSet(queryset= Order.objects.none(), instance=customerBasedOnId)

    # modelForm = OrderForm(initial={'customer': customerBasedOnId}) # Fetched model - OrderForm() from form.py


    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customerBasedOnId)

        if formset.is_valid():
            formset.save()
            return redirect('/')


    context = {
        'showForm': formset
    }
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):

    orderBasedOnId  = Order.objects.get(id=pk)
    modelForm       = OrderForm(instance=orderBasedOnId)

    if request.method == 'POST':
        
        modelForm = OrderForm(request.POST, instance=orderBasedOnId)

        if modelForm.is_valid():
            modelForm.save()
            return redirect('/')

    context = {
        'showForm': modelForm
    }
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    orderBasedOnId  = Order.objects.get(id=pk)  

    if request.method == "POST":
        orderBasedOnId.delete()
        return redirect('/')
        
    context = {
        'deleteItem': orderBasedOnId
    }
    return render(request, 'accounts/delete.html', context)
