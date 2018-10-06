from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

# Register your models here.
models = [UserProfile]
admin.site.register(models)