from django.urls import path
from . import views

urlpatterns = [
    path('howners/', views.hotel_owner_list_create),
    path('howners/<int:pk>/', views.hotel_owner_detail),

    # path('vehicles/', views.vehicle_list_create),
    # path('vehicles/<int:pk>/', views.vehicle_detail),

    # path('hreviews/', views.review_list_create),
    # path('hreviews/<int:pk>/', views.review_detail),
]
