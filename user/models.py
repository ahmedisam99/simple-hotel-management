from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'email', 'password')

    def __str__(self):
        return self.first_name + " " + self.last_name
