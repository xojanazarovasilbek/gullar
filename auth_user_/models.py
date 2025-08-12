from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True, unique=True)


    def __str__(self):
        return self.username