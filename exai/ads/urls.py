from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.index, name='index'),
    path('ads/<slug:pk>/', views.ads_detail),
]
