from django.db import models
from users.models import User

# Create your models here.
class Log(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']


class Collaborator(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
    mother = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mother")
