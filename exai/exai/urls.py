from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ads.urls', namespace='ads')),
    path('admin/', admin.site.urls),
]
