from django.contrib import admin
from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('api/<int:id>', views.user_api_list_work_desk, name='account_api_detail'),
]
