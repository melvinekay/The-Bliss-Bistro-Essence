from django.contrib import admin
from django import forms
from BlissBistroApp.models import Booking, Order, ImageModel, Subscriber


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

# class OrderAdminForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#
#     def clean(self):
#         cleaned_data = super().clean()
#         item = cleaned_data.get("item")
#         quantity = cleaned_data.get("quantity")
#
#         if item and quantity:
#             cleaned_data["total_price"] = item.price * quantity
#         return cleaned_data
