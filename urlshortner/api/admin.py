from django.contrib import admin
from .models import URL,User

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display  = ["username","email","created_at","last_login",'password']
    
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(URL)