from django.urls import path
from . import views

urlpatterns = [
    path('vowners/', views.vehicle_owner_list_create),
    path('vowners/<int:pk>/', views.vehicle_owner_detail),

    path('vehicles/', views.vehicle_list_create),
    path('vehicles/<int:pk>/', views.vehicle_detail),

    path('vreviews/', views.review_list_create),
    path('vreviews/<int:pk>/', views.review_detail),
]
