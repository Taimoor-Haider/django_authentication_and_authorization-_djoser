from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,name,is_admin=False,password=None):
        if not email:
            raise ValueError("Email is required")
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            is_admin = is_admin
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,is_admin=True,password=None):
        user = self.model(
            email=email,
            password=password,
            name=name,
            is_admin=is_admin
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        max_length=255
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','is_admin']

    objects=UserManager()

    def has_perm(self, perm, obj=None):
        return True  # or some custom logic

    def has_module_perms(self, app_label):
        return True  # or some custom logic

    def __str__(self):
        return self.email