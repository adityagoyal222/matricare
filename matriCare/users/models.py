from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):

    
    # Boolean Fields for determining user types
    USER_CHOICES=(
        (1,"Doctor"),
        (2,"Mother")
    )



    user_type=models.PositiveIntegerField(choices=USER_CHOICES,default=2)

    user_color= models.CharField(max_length=20,default='')

    # String representation of the User model
    def __str__(self):
        return self.username