from django.contrib import admin
from .models import Category, Book, Cart, OrderItem
from .models import Comment


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Comment)
admin.site.register(OrderItem)
# admin.site.register(Order)