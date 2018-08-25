from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Change_type(models.Model):
    Type_name = models.CharField(max_length=200)
    def __str__(self):
        return self.Type_name

class Change_content(models.Model):
    game_url = models.ForeignKey(Change_type, on_delete=models.CASCADE)
    Change_text = models.CharField(max_length=200)
    def __str__(self):
        return self.Change_text
class User(models.Model):
    username = models.CharField(max_length= 100)
    password = models.CharField(max_length= 100)
    level = models.IntegerField()
    def __str__(self):
        return self.username