from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg' , upload_to ='profile_pics')
    county = models.CharField(default = '', max_length=100)
    school = models.CharField(default = '', max_length=100)
    sport = models.CharField(default = '', max_length=100)
    height = models.CharField(default = '', max_length=100)
    weight = models.CharField(default = '', max_length=100)
    speed = models.CharField(default = '', max_length=100)
    age = models.CharField(default = '', max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args , **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
