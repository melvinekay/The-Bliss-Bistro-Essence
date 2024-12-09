from django.contrib import admin
from BlissBistroApp.models import Member, Product, Booking, Contact, User, Subscriber, FoodItem, Order, ImageModel
# from BlissBistroApp.forms import OrderAdminForm

# Register your models here.
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Subscriber)
admin.site.register(FoodItem)
admin.site.register(Order)
admin.site.register(ImageModel)

# class OrderAdmin(admin.ModelAdmin):
#     form = OrderAdminForm
#     readonly_fields = ['total_price']
#     list_display = ['item', 'quantity', 'total_price']
#
#     class Media:
#         js = 'admin/js/admin.js'