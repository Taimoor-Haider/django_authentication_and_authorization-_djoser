from django.db import models
from django.conf import settings
# Create your models here.

class HotelOwner(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="hotel_owner_profile")
    date_of_birth=models.CharField(max_length=255)

class Hotel(models.Model):
    user = models.ForeignKey("HotelOwner",on_delete=models.CASCADE,related_name="hotels")
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    number_of_rooms=models.PositiveIntegerField()


class HotelReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="hotel_reviews")
    hotel= models.OneToOneField(Hotel,on_delete=models.CASCADE,related_name='hotel_reviews')
    rating = models.PositiveSmallIntegerField()  
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)