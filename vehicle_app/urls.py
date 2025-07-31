from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.vehicle_owner_list_create),
    path('owners/<int:pk>/', views.vehicle_owner_detail),

    path('vehicles/', views.vehicle_list_create),
    path('vehicles/<int:pk>/', views.vehicle_detail),

    path('reviews/', views.review_list_create),
    path('reviews/<int:pk>/', views.review_detail),
]
