from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    birthday_year = models.PositiveIntegerField(default=2000)
