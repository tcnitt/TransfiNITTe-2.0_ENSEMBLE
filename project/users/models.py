from django.db import models
from django.contrib.auth.models import AbstractUser

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

    REQUIRED_FIELDS = ['first_name','last_name','email','year','department','cgpa','github_link','linkedin_link','resume_link','transcript_link','areas_of_interest']

    def __str__(self):
        return self.get_full_name()+' - '+self.username