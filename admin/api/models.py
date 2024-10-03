from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return json.dumps({
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'complete': self.complete,
            'user': self.user.username,  # Displaying username instead of user id in the admin panel.
        })
    
    class Meta:
        ordering = ['complete']

class UserRefreshToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='refresh_token')
    refresh_token = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s refresh token"