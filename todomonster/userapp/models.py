from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    birthday_year = models.PositiveIntegerField(default=2000)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday_year}'
