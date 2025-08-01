from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny 
from rest_framework.views import APIView
from .models import VehicleOwner, Vehicle, VehicleReview
from .serializers import VehicleOwnerSerializer, VehicleSerializer, VehicleReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
class VehicleOwnerViewSet(ModelViewSet):
    queryset = VehicleOwner.objects.all()
    serializer_class = VehicleOwnerSerializer

    def perform_destroy(self, instance):
        if instance.vehicles.exists():
            raise ValidationError({'error': 'Vehicle owner cannot be deleted because they own vehicles.'})
        instance.delete()

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class ReviewViewSet(ModelViewSet):
    queryset = VehicleReview.objects.all()
    serializer_class = VehicleReviewSerializer
