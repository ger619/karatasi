from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    position = models.CharField(max_length=100)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.position
