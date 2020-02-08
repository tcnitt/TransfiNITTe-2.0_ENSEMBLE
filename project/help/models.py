from django.db import models
import os

HELP_PHOTO_PATH = 'help_photos'
DEFAULT_HELP_PHOTO = os.path.join(HELP_PHOTO_PATH,'default_help.png')


# Create your models here.
class help(models.Model):
    title = models.CharField(max_length=200,help_text='Title of article')
    description = models.CharField(max_length=300,help_text='Short description of article')
    image = models.ImageField(upload_to=HELP_PHOTO_PATH,default=DEFAULT_HELP_PHOTO)
    link = models.URLField(max_length=200,help_text='Link to article')
    author = models.CharField(max_length=200,help_text='Name of author')


    def __str__(self):
        return self.title
