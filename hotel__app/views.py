from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny 

from .models import Hotel, HotelOwner, HotelReview
from .serializers import HotelOwnerSerializer, HotelReviewSerizlizer, HotelSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def hotel_owner_list_create(request):
    if request.method == "GET":
        hotel_owners = HotelOwner.objects.all()
        serializer = HotelOwnerSerializer(hotel_owners, many=True)
        # print(request.user.email)
        # print(request.user.is_active)
        # print(request.user.is_staff)
        # print(request.user.id)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HotelOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def hotel_owner_detail(request, pk):
    try:
        hotel_owner = HotelOwner.objects.get(pk=pk)
    except HotelOwner.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=404)
    
    serializer = HotelOwnerSerializer(hotel_owner)
    return Response(serializer.data)


