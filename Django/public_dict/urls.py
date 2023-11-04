from django.contrib import admin
from django.urls import path
from public_dict import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('',  views.home, name='home2'),
    path('words_list/', views.show, name='words_list'),
    path('add_word/', views.add, name='add_word')
]