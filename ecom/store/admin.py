from django.contrib import admin



# Register your models here.

from .models import Customer
admin.site.register(Customer)

from .models import  Product
admin.site.register (Product)

from .models import  Order
admin.site.register( Order )

from .models import  OrderItem
admin.site.register( OrderItem )

from .models import ShippingAddress
admin.site.register( ShippingAddress )