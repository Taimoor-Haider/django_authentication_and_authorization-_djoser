from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, name, user_type='customer', password=None, is_admin=False):
        if not email:
            raise ValueError("Email is required")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            user_type=user_type,
            is_admin=is_admin
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email=email,
            name=name,
            password=password,
            is_admin=True
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('vehicle', 'Vehicle Owner'),
        ('hotel', 'Hotel Owner'),
        ('travel', 'Travel Club Owner'),
    ]

    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='customer',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
