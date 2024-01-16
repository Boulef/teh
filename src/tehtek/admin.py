# admin.py
from django.contrib import admin
from .models import Laptop, Desktop, AllInOne, Tablet, Part, OtherProduct, Accessorie

admin.site.register(Laptop)
admin.site.register(Desktop)
admin.site.register(AllInOne)
admin.site.register(Tablet)
admin.site.register(Part)
admin.site.register(OtherProduct)
admin.site.register(Accessorie)