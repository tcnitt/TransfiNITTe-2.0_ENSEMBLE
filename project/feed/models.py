from django.db import models
from django.contrib.auth import get_user_model
import os 
from taggit.managers import TaggableManager
from datetime import datetime
# Create your models here.


POST_PHOTO_PATH = 'post_photos/%d/%m/%Y'
DEFAULT_POST_PHOTO = os.path.join('post_photos/default.jpg')

class post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_photos/%d/%m/%Y',blank=True,default=DEFAULT_POST_PHOTO)
    tags = TaggableManager()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title