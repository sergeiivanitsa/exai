from django.contrib import admin
from .models import Car, Transmission, Drive, Configuration, Image

admin.site.register(Car)
admin.site.register(Transmission)
admin.site.register(Drive)
admin.site.register(Configuration)
admin.site.register(Image)
