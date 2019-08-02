from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pos-home'),
    path('customer_info/', views.customer_information, name='pos-customer-info'),
    path('customer_info/<phone_number>/', views.customer_information, name='pos-customer-info'),
    path('new_ticket/', views.new_ticket, name='pos-new-ticket')
]
