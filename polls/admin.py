from django.contrib import admin

from .models import Inputs, Problems, Submission,Userss

admin.site.register(Problems)
admin.site.register(Inputs)
admin.site.register(Submission)
admin.site.register(Userss)