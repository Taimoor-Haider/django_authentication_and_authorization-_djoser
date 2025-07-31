from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import VehicleOwner, Vehicle, VehicleReview
from .serializers import VehicleOwnerSerializer, VehicleSerializer, VehicleReviewSerializer



@api_view(['GET', 'POST'])
def vehicle_owner_list_create(request):
    if request.method == 'GET':
        owners = VehicleOwner.objects.all()
        serializer = VehicleOwnerSerializer(owners, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VehicleOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vehicle_owner_detail(request, pk):
    try:
        owner = VehicleOwner.objects.get(pk=pk)
    except VehicleOwner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehicleOwnerSerializer(owner)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehicleOwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def vehicle_list_create(request):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vehicle_detail(request, pk):
    try:
        vehicle = Vehicle.objects.get(pk=pk)
    except Vehicle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list_create(request):
    if request.method == 'GET':
        reviews = VehicleReview.objects.all()
        serializer = VehicleReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VehicleReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    try:
        review = VehicleReview.objects.get(pk=pk)
    except VehicleReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehicleReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehicleReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
