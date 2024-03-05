from django.contrib import admin
from .models import Cars, CarsSold, Brand, Customers

admin.site.register(Cars)
admin.site.register(Brand)
admin.site.register(Customers)
admin.site.register(CarsSold)
