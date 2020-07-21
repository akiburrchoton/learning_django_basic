from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory # formset - multiple forms in a single form
from django.contrib.auth.forms import UserCreationForm # djnago user form - we can customise it by ourself
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #flash message - one time message 
from django.contrib.auth.decorators import login_required # to maintain the user resctriction
from django.contrib.auth.models import Group 

from .models import *
from .forms import *
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only



# Create your views here.

@unauthenticated_user
def registerPage(request):
    regForm    = CreateUserForm() # CreateUserForm - my customised form in forms.py

    if request.method == "POST":
        regForm    = CreateUserForm(request.POST)

        if regForm.is_valid():
            user    = regForm.save()
            newUser = regForm.cleaned_data.get('username') # The user which was created in register form
            messages.success(request, 'Account was created for ' + newUser ) # Success Message

            # group   = Group.objects.get(name='customer')
            # user.groups.add(group) 

            # make the user role to customer when they sign up
            # Customer.objects.create(
            #     user = user,
            # )
            return redirect('showUrlLogin') # In redirect I must use the name="something" which I used in urls.py

    context ={
        'showRegForm': regForm,
    }
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        fetchedUsername     = request.POST.get('username')
        fetchedPassword     = request.POST.get('password')

        authenticatedUser   = authenticate(request, username=fetchedUsername, password=fetchedPassword)

        if authenticatedUser is not None:
            login(request, authenticatedUser) # This login() method is django built in
            return redirect('showUrlHome') # In redirect I must use the name="something" which I used in urls.py
        else:
            messages.info(request, 'Username or Password is incorrect!')
    
    
    context = {

    }
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('showUrlLogin')

@login_required(login_url='showUrlLogin') # Restricting users who are not logged in
@admin_only # checks if admin or customer
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

@login_required(login_url='showUrlLogin') # Restricting users who are not logged in
@allowed_users(allowed_roles=['customer']) # checks if customer 
def userPage(request):
    allOrders       = request.user.customer.order_set.all()

    totalOrders     = allOrders.count()
    
    delivered       = allOrders.filter(status="Delivered").count()
    pending         = allOrders.filter(status="Pending").count()

    context = {
        'showAllOrder': allOrders, 
        'total_orders': totalOrders, 
        'delivered': delivered, 
        'pending': pending
    }
    return render(request, 'accounts/user.html', context)
    

@login_required(login_url='showUrlLogin') # Restricting users who are not logged in
@allowed_users(allowed_roles=['customer']) # checks if customer 
def accountSettings(request):
    customer    = request.user.customer
    form        = CustomerFrom(instance=customer)

    if request.method == 'POST':
        form    = CustomerFrom(request.POST, request.FILES, instance=customer)

        if form.is_valid:
            form.save()


    context = {
        'showAccountForm' : form 
    }
    return render(request, 'accounts/account_settings.html', context)



@login_required(login_url='showUrlLogin')
@allowed_users(allowed_roles=['admin'])
def products(request):
    allProducts = Product.objects.all()

    context     = {
        'products' : allProducts
    }

    return render(request, 'accounts/products.html', context)
    

@login_required(login_url='showUrlLogin') # Restricting users who are not logged in    
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='showUrlLogin') # Restricting users who are not logged in
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='showUrlLogin') # Restricting users who are not logged in
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='showUrlLogin') # Restricting users who are not logged in
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    orderBasedOnId  = Order.objects.get(id=pk)  

    if request.method == "POST":
        orderBasedOnId.delete()
        return redirect('/')
        
    context = {
        'deleteItem': orderBasedOnId
    }
    return render(request, 'accounts/delete.html', context)
