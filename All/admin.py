from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Items)
admin.site.register(ShippingAddress)
admin.site.register(Message)