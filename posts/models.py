from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/", blank=True)
    
class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    edited_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=101)
    content = models.TextField()
    read_by = models.ManyToManyField(User, related_name="read_messages", blank=True)