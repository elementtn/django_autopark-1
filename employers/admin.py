from django.contrib import admin
from .models import Department, Position, Car, CarBrand


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(CarBrand)
admin.site.register(Car)
