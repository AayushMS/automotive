import random
from curses.ascii import US
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

def generate_random_vehicle_number():
    return "".join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(10)])

class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    TYPE_CHOICES = (
        ("HATCHBACK", "Hatchback"),
        ("SEDAN", "Sedan"),
        ("SUV", "suv"),
        ("COUPE", "Coupe"),
        ("CROSSOVER", "Crossover"),
    )
    
    
    vehicle_no = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    manufactured_date = models.DateField()
    brand = models.ForeignKey(
        Brand, related_name='vehicle_brand', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='vehicle_created_by', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='media/vehicles/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.vehicle_no} {self.brand} {self.model}"
    
class Parts(models.Model):
    name = models.CharField(max_length=255)
    manufactuer = models.CharField(max_length=255)
    quantity = models.IntegerField()
    created_by = models.ForeignKey(
        User, related_name='part_created_by', on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"