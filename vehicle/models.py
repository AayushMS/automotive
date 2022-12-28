from django.db import models

# Create your models here.

class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    manufactured_date = models.DateField()
    
    def __str__(self):
        return f"{self.brand} {self.model}"