from django.db import models
from django.contrib.auth.models import AbstractUser

from projects.models import projects

import os 

YEAR_CHOICES = (
    (2,"2nd"),
    (3,"3rd"),
    (4,"4th"),
)

DEPT_CHOICES = (
    ("CHEM","Chemical Engineering"),
    ("CSE","Computer Science and Engineering"),
    ("CIVIL","Civil Engineering"),
    ("EEE","Electrical and Electronics Engineering"),
    ("ECE","Electronics and Communications Engineering"),
    ("ICE","Instrumentation and Control Engineering"),
    ("MECH","Mechanical Engineering"),
    ("META","Metallurgical and Materials Engineering"),
    ("PROD","Production Engineering"),
)

USER_PHOTO_PATH = 'users_photo'
DEFAULT_USER_PHOTO = os.path.join(USER_PHOTO_PATH,'default_user.jpg')

FEEDBACK_RATINGS = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

DEFAULT_RATING = '3'
# Create your models here.
class user(AbstractUser):
    year = models.IntegerField(choices=YEAR_CHOICES)
    department = models.CharField(choices=DEPT_CHOICES,max_length=200)
    cgpa = models.DecimalField(max_digits=3,decimal_places=2)
    github_link = models.URLField(max_length=200,default='',help_text='Link to GitHub profile')
    linkedin_link = models.URLField(max_length=200,help_text='Link to LinkedIn profile')
    resume_link = models.URLField(max_length=200,help_text='Link to Resume')
    transcript_link = models.URLField(max_length=200,help_text='Link to Transcript')
    areas_of_interest = models.CharField(max_length=200,help_text='Areas of interest')
    photo = models.ImageField(upload_to=DEFAULT_USER_PHOTO,default=DEFAULT_USER_PHOTO)
    bio = models.CharField(max_length=300,blank=True,help_text='Enter short bio(max 300 chars)')
    projects = models.ManyToManyField(projects,blank=True)



    REQUIRED_FIELDS = ['first_name','last_name','email','year','department','cgpa','github_link','linkedin_link','resume_link','transcript_link','areas_of_interest']

    def __str__(self):
        return self.get_full_name()+' - '+self.username

    def get_areas_of_interest(self):
        return self.areas_of_interest.split(",")


class professor(models.Model):
    name = models.CharField(max_length=200,help_text='Enter your full name')
    email = models.EmailField(help_text='Enter your institute e-mail')
    password = models.CharField(max_length=200,help_text='Enter password')
    department = models.CharField(choices=DEPT_CHOICES,max_length=200)
    research_areas = models.CharField(max_length=200,help_text='Enter comma separated Areas of research')
    google_scholar = models.CharField(max_length=200,blank=True,help_text='Enter your Google scholar ID')
    photo = models.ImageField(upload_to=DEFAULT_USER_PHOTO,default=DEFAULT_USER_PHOTO)

    REQUIRED_FIELDS = ['first_name','last_name','email','department','research_areas']

    def __str__(self):
        return self.name


    def get_research_areas(self):
        return self.research_areas.split(",")



class feedback(models.Model):
    contributor = models.OneToOneField(user,on_delete=models.CASCADE,related_name='feedback')
    project = models.OneToOneField(projects,on_delete=models.CASCADE,related_name='feedback')
    comment = models.CharField(max_length=300,help_text='Feedback')
    rating = models.CharField(max_length=2,choices=FEEDBACK_RATINGS,default=DEFAULT_RATING)

    def __str__(self):
        return self.contributor.get_full_name()+ '-' + self.project.title