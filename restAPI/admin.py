from django.contrib import admin
from .models import Department,JobPosition,Profile,Patient


my_apps = [Department,JobPosition,Profile,Patient]

admin.site.register(my_apps)
