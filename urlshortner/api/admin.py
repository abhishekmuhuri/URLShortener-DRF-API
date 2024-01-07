from django.contrib import admin
from .models import URL, User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(URL)
