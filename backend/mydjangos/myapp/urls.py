from django.urls import path
import myapp.views as views
from django.contrib import admin
from .views import TaskList

urlpatterns = [
    path('data_view/', TaskList.as_view(), name='myapp'),
]