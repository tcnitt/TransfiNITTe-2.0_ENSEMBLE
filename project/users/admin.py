from django.contrib import admin

from .models import user,professor,feedback
# Register your models here.


admin.site.register(professor)
admin.site.register(user)
admin.site.register(feedback)
