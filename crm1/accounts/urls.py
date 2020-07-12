from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="showUrlHome"),
    path('products/', views.products, name="showUrlProduct"),
    path('customer/<str:pk_test>/', views.customer, name="showUrlCustomer"),
    path('create-order/<str:pk>/', views.createOrder, name="showUrlCreateOrder"),
    path('update-order/<str:pk>/', views.updateOrder, name="showUrlUpdateOrder"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="showUrlDeleteOrder")

]

