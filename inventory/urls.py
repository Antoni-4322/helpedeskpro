from django.contrib import admin
from django.urls import path
from ticket import views

app_name = 'inventory'

urlpatterns = [
    path('', views.MyTickets.as_view(), name='home'),
]
