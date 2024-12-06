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