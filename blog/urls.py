from django.contrib import admin
from django.urls import path
from blog.views import index, carreira

urlpatterns = [
    path('', index, name='index') ,
    path('carreira/', carreira, name='carreira')
]
