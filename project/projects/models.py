from django.db import models


# Create your models here.

BODIES = (
    ('Delta','Delta'),
    ('Spider','Spider'),
    ('DataByte','DataByte'),
    ('DC','Designer’s Consortium'),
    ('Builders’ Hive','Builders’ Hive'),
    ('3D','3rd Dimension Aeromodelling Club'),
    ('RMI','RMI – Robotics and Machine Intelligence'),
    ('CSE','Computer Science & Engineering dept'),
    ('CIVIL','Civil Engineering dept'),
    ('CHEM','Chemical Engineering dept'),
    ('EEE','Electrical and Electronics Engineering dept'),
    ('ECE','Electronics and Communications Engineering dept'),
    ('ICE','Instrumentation & Control Eningeering dept'),
    ('MECH','Mechanical Engineering dept'),
    ('PROD','Production Eningeering dept'),
    ('META','Metallurgical Eningeering dept'),
)

DEFAULT_BODY = 'CSE'

PROJECT_STATUS = (
    ('1','Not yet started'),
    ('2','In progress'),
    ('3','Completed'),
)

DEFAULT_PROJECT_STATUS = '1'

DEGREE_CHOICES = (
    ('B.Tech','B.Tech'),
    ('M.Tech','M.Tech'),
    ('PhD','PhD'),
    ('All','All'),
)

DEFAULT_DEGREE = 'All'

PROJECT_DURATION = (
    ('1','1 month'),
    ('2','2 months'),
    ('3','3 months'),
    ('4','5 months'),
    ('6','6 months'),
    ('7','>6 months'),
)

DEFAULT_PROJECT_DURATION = '6'

class projects(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    domain = models.CharField(max_length=300,help_text='Enter domains as comma separated values')
    author = models.CharField(max_length=50,help_text='Name of person to contact')
    phone = models.CharField(max_length=10,help_text='Enter 10-digit phone no.')
    email = models.EmailField()
    prerequisites = models.TextField(help_text='Enter pre-requisites as comma separated values')
    body = models.CharField(choices=BODIES,max_length=100,default=DEFAULT_BODY)
    status = models.CharField(max_length=50,choices=PROJECT_STATUS,default=DEFAULT_PROJECT_STATUS)
    degree = models.CharField(max_length=20,choices=DEGREE_CHOICES,default=DEFAULT_DEGREE)
    duration = models.CharField(max_length=20,choices=PROJECT_DURATION,default=DEFAULT_PROJECT_DURATION)
    link = models.URLField(max_length=200,blank=True,help_text='Links if any')
    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'


    def __str__(self):
        return self.title

    def domains_list(self):
        return self.domain.split(',')

    def prerequisites_list(self):
        return self.prerequisites.split(',')