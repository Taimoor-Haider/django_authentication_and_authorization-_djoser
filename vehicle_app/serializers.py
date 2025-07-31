from rest_framework import serializers
from .models import VehicleOwner, Vehicle, VehicleReview
from django.contrib.auth import get_user_model

User = get_user_model()

class VehicleOwnerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_info = serializers.StringRelatedField(source='user', read_only=True)

    class Meta:
        model = VehicleOwner
        fields = ['id', 'user', 'user_info', 'license_number', 'vehicle_type']


class VehicleSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=VehicleOwner.objects.all(), write_only=True)
    owner_info = VehicleOwnerSerializer(source='owner', read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'owner', 'owner_info', 'make', 'model', 'year', 'license_plate', 'color']


class VehicleReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_info = serializers.StringRelatedField(source='user', read_only=True)
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), write_only=True)
    vehicle_info = VehicleSerializer(source='vehicle', read_only=True)

    class Meta:
        model = VehicleReview
        fields = ['id', 'user', 'user_info', 'vehicle', 'vehicle_info', 'rating', 'comment', 'created_at']
        read_only_fields = ['created_at']
