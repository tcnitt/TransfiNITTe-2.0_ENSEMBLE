from django.db import models
from django.contrib.auth import get_user_model
import os 
# Create your models here.


POST_PHOTO_PATH = 'post_photos/%d/%m/%Y'
DEFAULT_POST_PHOTO = os.path.join(POST_PHOTO_PATH,'default.jpg')

class post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=POST_PHOTO_PATH,blank=True,default=DEFAULT_POST_PHOTO)