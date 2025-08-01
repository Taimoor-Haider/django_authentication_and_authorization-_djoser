from django.urls import path, include 
from . import views
from rest_framework.routers import SimpleRouter
from pprint import pprint

router = SimpleRouter()
router.register("vowners", views.VehicleOwnerViewSet)
router.register("vehicles", views.VehicleViewSet)
router.register("vreviews", views.ReviewViewSet)

pprint(router.urls) 

urlpatterns = [
    path("", include(router.urls)), 
]
