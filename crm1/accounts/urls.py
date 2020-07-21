from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="showUrlRegister"),
    path('login/', views.loginPage, name="showUrlLogin"),
    path('logout/', views.logoutUser, name="showUrlLogout"),
    
    path('', views.home, name="showUrlHome"),
    path('user/', views.userPage, name="showUrlUserpage"),
    
    path('account/', views.accountSettings, name="showUrlAccount"),

    path('products/', views.products, name="showUrlProduct"),
    path('customer/<str:pk_test>/', views.customer, name="showUrlCustomer"),

    path('create-order/<str:pk>/', views.createOrder, name="showUrlCreateOrder"),
    path('update-order/<str:pk>/', views.updateOrder, name="showUrlUpdateOrder"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="showUrlDeleteOrder"),


    # Password Reset URLS(default)
    path('reset-password/', 
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), 
    name="reset_password"),
    path('reset-password-sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
    name="password_reset_done"),
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
    name="password_reset_confirm"), # uidb64 - is user id based on 64 bit
    path('reset-password-complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
    name="password_reset_complete"),
    
]

