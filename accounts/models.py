

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
 
 
class CustomUser(AbstractUser):
    game_status = models.IntegerField(null=True)