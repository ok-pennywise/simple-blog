from datetime import datetime
from django.db import models
from .validators import validate_email


# Create your models here.
class User(models.Model):
    email: str = models.CharField(
        max_length=256, unique=True, validators=(validate_email,)
    )
    full_name: str = models.CharField(max_length=100)

    date_joined: datetime = models.DateTimeField(auto_now_add=True)

    password: str = models.CharField(max_length=256)

    class Meta:
        indexes = [models.Index(fields=["email"])]
