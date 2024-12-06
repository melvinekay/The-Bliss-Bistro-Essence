from django.db import models

# Create your models here.
class Member(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    yob = models.DateField()

    def __str__(self):
        return self.full_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True)  # Field to associate orders with a session
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} (Session: {self.session_key})"

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title