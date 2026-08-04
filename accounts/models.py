from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
class User(AbstractUser):
    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        blank=True,
        null=True
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()
    def __str__(self):
        return self.get_full_name() or self.email