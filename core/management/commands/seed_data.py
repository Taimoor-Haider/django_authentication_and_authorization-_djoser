# core/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from vehicle_app.models import VehicleOwner, Vehicle, VehicleReview
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with dummy data"

    def handle(self, *args, **kwargs):
        # Create users
        for i in range(5):
            user, created = User.objects.get_or_create(
                email="testuser@example.com",
                defaults={
                    "name": "Test User",
                    "password": "123456",
                    "user_type": "vehicle",
                    "is_active": True
                }
            )
            if created:
                user.set_password("password123")
                user.save()

            # Create VehicleOwner
            owner, _ = VehicleOwner.objects.get_or_create(
                user=user,
                defaults={
                    "license_number": f"LIC-{i}23",
                    "vehicle_type": random.choice(["Sedan", "SUV", "Bike"])
                }
            )

            # Create Vehicle
            for j in range(2):  # each owner gets 2 vehicles
                vehicle, _ = Vehicle.objects.get_or_create(
                    owner=owner,
                    license_plate=f"PLATE-{i}{j}",
                    defaults={
                        "make": "Toyota",
                        "model": f"Model-{j}",
                        "year": 2020 + j,
                        "color": random.choice(["Red", "Blue", "Black"])
                    }
                )

                # Create VehicleReview
                VehicleReview.objects.get_or_create(
                    user=user,
                    vehicle=vehicle,
                    defaults={
                        "rating": random.randint(1, 5),
                        "comment": f"This is a review for vehicle {vehicle.license_plate}"
                    }
                )

        self.stdout.write(self.style.SUCCESS("Dummy data seeded successfully."))
