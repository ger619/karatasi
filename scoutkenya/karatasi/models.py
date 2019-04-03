from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.db import models


class Post(models.Model):
    sport_type = (('soccer', 'Soccer'),('basketball', 'Basketball'),('netball', 'Netball'),)
    image = models.ImageField(default = 'default.jpg' , upload_to ='player_pics')
    county = models.CharField(default = '', max_length=100)
    school = models.CharField(default = '', max_length=100)
    player_name = models.CharField(default = '', max_length=100)
    age = models.CharField(default = '', max_length=100)
    gender = models.CharField(default = '', max_length=100)
    sport =  models.CharField(max_length=10, choices=sport_type)
    height = models.CharField(default = '', max_length=100)
    weight = models.CharField(default = '', max_length=100)
    speed = models.CharField(default = '', max_length=100)
    position = models.CharField(max_length=100)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Post'

    def save(self, *args , **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
