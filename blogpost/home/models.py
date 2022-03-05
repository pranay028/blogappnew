from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from django.contrib.auth.models import User,auth
# Create your models here.

class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return f"{self.title}- {self.user}"