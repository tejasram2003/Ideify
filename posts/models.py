from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    post_time = models.DateTimeField(default= datetime.now, blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    def __str__(self):
        return str(self.user)
    

