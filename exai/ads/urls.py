from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('ads/<slug:pk>/', views.ads_detail),
]
