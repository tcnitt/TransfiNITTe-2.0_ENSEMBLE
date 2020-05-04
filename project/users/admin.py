from django.contrib import admin

from .models import Users,Professor,Student,Feedback
# Register your models here.


admin.site.register(Professor)
admin.site.register(Users)
admin.site.register(Student)
