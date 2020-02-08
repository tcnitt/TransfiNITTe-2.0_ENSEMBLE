from django.db import models

# Create your models here.
class faq(models.Model):
    question = models.TextField(help_text='Question')
    answer = models.TextField(help_text='Answer')


    def __str__(self):
        return self.question