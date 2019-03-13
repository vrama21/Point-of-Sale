from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pos-home'),
    path('customer_info_blank/', views.customer_information_blank, name='pos-customer-info-blank'),
    path('customer_info/<customer_phone_num>/', views.customer_information, name='pos-customer-info'),
    path('new_ticket/', views.new_ticket, name='pos-new-ticket')
]