from django.db import models
from GetItApp.models import Product
from  django.utils.timezone import datetime, timedelta
# Create your models here.

class Order(models.Model):
    BUILDINGS = (
        ('Quintal', 'Quintal'),
        ('2 Herb Street', '2 Herb Street'),
        ('Miller', 'Miller'),
    )
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=250,)
    cell_number = models.CharField(max_length=10)
    building = models.CharField(max_length=100,choices=BUILDINGS)
    room_number = models.CharField(max_length=5)
    additional_notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def return_delivery():
        now = datetime.now()
        return now + timedelta(minutes=30)
    delivery = models.TimeField(default=return_delivery)

    class Meta():
        ordering = ('-created',)
    
    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in item.self.all())

class Ordered_item(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ordered_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10 ,decimal_places=2,)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
        
    def get_cost(self):
        return self.price * self.quantity

class ServiceOrder(models.Model):
    BUILDINGS = (
        ('Quintal', 'Quintal'),
        ('2 Herb Street', '2 Herb Street'),
        ('Miller', 'Miller'),
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=250,)
    building = models.CharField(max_length=100, choices=BUILDINGS)
    number = models.CharField(max_length=10)
    room_number = models.CharField(max_length=5)
    ordered_product = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)


    def __str__(self):
        return self.name

class SpecialOrder(models.Model):
    BUILDINGS = (
        ('Quintal', 'Quintal'),
        ('2 Herb Street', '2 Herb Street'),
        ('Miller', 'Miller'),
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=250,)
    building = models.CharField(max_length=100, choices=BUILDINGS)
    number = models.CharField(max_length=10)
    room_number = models.CharField(max_length=5)
    ordered_product = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)


    def __str__(self):
        return self.name