from django.db import models
from users.models import user
# Create your models here.

BODIES = (
    ('Delta','Delta'),
    ('Spider','Spider'),
    ('DataByte','DataByte'),
    ('CSE','Computer Science & Engineering dept'),
    ('CIVIL','Civil Engineering dept'),
    ('CHEM','Chemical Engineering dept'),
    ('EEE','Electrical and Electronics Engineering dept'),
    ('ECE','Electronics and Communications Engineering dept'),
    ('MECH','Mechanical Engineering dept'),
)

DEFAULT_BODY = 'CSE'

class projects(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    domain = models.CharField(max_length=300,help_text='Enter domains as comma separated values')
    author = models.CharField(max_length=50,help_text='Name of person to contact')
    phone = models.CharField(max_length=10,help_text='Enter 10-digit phone no.')
    email = models.EmailField()
    prerequisites = models.TextField(help_text='Enter pre-requisites as comma separated values')
    body = models.CharField(choices=BODIES,max_length=100,default=DEFAULT_BODY)


    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'


    def __str__(self):
        return self.title

    def domains_list(self):
        return self.domain.split(',')

    def prerequisites_list(self):
        return self.prerequisites.split(',')