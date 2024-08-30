from datetime import datetime
from django.db import models

from users.models import User


# Create your models here.
class Blog(models.Model):
    title: str = models.CharField(max_length=1024)
    body: str = models.TextField()

    created_on: datetime = models.DateTimeField(auto_now_add=True)

    author: "User" = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    blog: "Blog" = models.ForeignKey(Blog, on_delete=models.CASCADE)
    media: str = models.ImageField()