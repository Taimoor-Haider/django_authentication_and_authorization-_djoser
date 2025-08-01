from .models import Hotel,HotelOwner,HotelReview
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.serializers import CustomUserSerializer
User=get_user_model()

class HotelOwnerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    user_info = CustomUserSerializer(source="user", read_only=True)
    class Meta:
        model = HotelOwner
        fields=["id","user","user_info","date_of_birth"]


class HotelSerializer(serializers.ModelSerializer):
    user =serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    user_info = serializers.StringRelatedField(source="user",read_only=True)
    class Meta:
        model = Hotel
        fields=["id","user","user_info","name","location","number_of_rooms"]



class HotelReviewSerizlizer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(),write_only=True)
    hotel = serializers.PrimaryKeyRelatedField(queryset = Hotel.objects.all(),write_only=True)
    user_info = serializers.StringRelatedField(source="user",read_only=True)
    hotel_info = serializers.StringRelatedField(source="hotel",read_only=True)
    class Meta:
        model = HotelReview
        fields = ["id","user","hotel","user_info","hotel_info","rating","comment","created_at"]
