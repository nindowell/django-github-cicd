from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=120, unique=True, blank=False, null=False, validators=[
        MinLengthValidator(3),
        MaxLengthValidator(110)
    ])
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.username
