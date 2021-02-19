from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Boolean Fields for determining user types
    is_doctor = models.BooleanField(default=False)
    is_mother= models.BooleanField(default=False)

    # String representation of the User model
    def __str__(self):
        return self.username