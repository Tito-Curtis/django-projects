from django.contrib import admin
from .models import meetings,room,Product,ProductImage,Category,All_Users


# Register your models here.
admin.site.register(meetings)
admin.site.register(room)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(All_Users)