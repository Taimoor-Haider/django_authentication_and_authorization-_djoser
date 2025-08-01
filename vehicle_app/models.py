from django.db import models
from django.conf import settings
# Create your models here.

class VehicleOwner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="vehicle_owner_profile")
    license_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)


class Vehicle(models.Model):
    owner = models.ForeignKey(
        'VehicleOwner', 
        on_delete=models.CASCADE,
        related_name='vehicles'
    )
    make = models.CharField(max_length=100)  
    model = models.CharField(max_length=100) 
    year = models.PositiveIntegerField()  
    license_plate = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=50)

class VehicleReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="vehicle_reviews")
    vehicle= models.OneToOneField(Vehicle,on_delete=models.CASCADE,related_name='vehicle_reviews')
    rating = models.PositiveSmallIntegerField()  
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

