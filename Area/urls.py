#from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('info/<int:id>/',info,name='info'),
    path('search/',search,name='search'),
    path('about/',about,name='about'),
]
