from django.contrib import admin
from . models import Product,Cart,Orders
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Orders)