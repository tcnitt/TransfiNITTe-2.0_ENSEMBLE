from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from projects.models import Projects

import os 
import enum

YEAR_CHOICES = (
    (1,"1st"),
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

# class Rating(enum.Enum):
#     POOR = 1
#     AVERAGE = 2
#     GOOD = 3
#     VERY_GOOD = 4
#     EXCELLENT = 5

# FEEDBACK_RATINGS = (
#     (Rating.POOR,       Rating.POOR.name),
#     (Rating.AVERAGE,    Rating.AVERAGE.name),
#     (Rating.GOOD,       Rating.GOOD.name),
#     (Rating.VERY_GOOD,  Rating.VERY_GOOD.name),
#     (Rating.EXCELLENT  ,Rating.EXCELLENT.name),
# )
# DEFAULT_RATING = Rating.AVERAGE

FEEDBACK_RATINGS = (
    (1,"Poor"),
    (2,"Average"),
    (3,"Good"),
    (4,"Very Good"),
    (5,"Excellent")
)

DEFAULT_RATING = 2

class Users(AbstractUser):

    is_student = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    department = models.CharField(choices=DEPT_CHOICES,max_length=200)

    def __str__(self):
        return self.email

# Create your models here.
class Student(Users):
    year = models.IntegerField(choices=YEAR_CHOICES)
    cgpa = models.DecimalField(max_digits=3,decimal_places=2)
    github_link = models.URLField(max_length=200,default='',help_text='Link to GitHub profile')
    linkedin_link = models.URLField(max_length=200,help_text='Link to LinkedIn profile')
    resume_link = models.URLField(max_length=200,help_text='Link to Resume')
    transcript_link = models.URLField(max_length=200,help_text='Link to Transcript')
    areas_of_interest = models.CharField(max_length=200,help_text='Areas of interest')
    photo = models.ImageField(upload_to=DEFAULT_USER_PHOTO,default=DEFAULT_USER_PHOTO)
    bio = models.CharField(max_length=300,blank=True,help_text='Enter short bio(max 300 chars)')
    projects = models.ManyToManyField(Projects,blank=True)

    REQUIRED_FIELDS = ['first_name','last_name','year','department','cgpa','github_link','linkedin_link','resume_link','transcript_link','areas_of_interest']

    def __str__(self):
        return self.get_full_name()

    def get_areas_of_interest(self):
        return self.areas_of_interest.split(",")

    def get_absolute_url(self):
        return reverse('users:profile',kwargs={"id":self.id})


    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

class Professor(Users):
    research_areas = models.CharField(max_length=200,help_text='Enter comma separated Areas of research')
    google_scholar = models.CharField(max_length=200,blank=True,help_text='Enter your Google scholar ID')
    photo = models.ImageField(upload_to=USER_PHOTO_PATH,default=DEFAULT_USER_PHOTO)

    REQUIRED_FIELDS = ['first_name','last_name','department','research_areas']

    def __str__(self):
        return self.get_full_name()


    def get_research_areas(self):
        return self.research_areas.split(",")

    def save(self, *args, **kwargs): 
        self.is_student = False
        super(Professor, self).save(*args, **kwargs) 
        
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

class Feedback(models.Model):
    contributor = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='feedback')
    project = models.OneToOneField(Projects,on_delete=models.CASCADE,related_name='feedback')
    comment = models.CharField(max_length=300,help_text='Feedback')
    rating = models.IntegerField(choices=FEEDBACK_RATINGS,default=DEFAULT_RATING)

    def __str__(self):
        return self.contributor.get_full_name()+ '-' + self.project.title