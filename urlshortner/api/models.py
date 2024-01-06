from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token
from re import sub

class User(models.Model):
    username = models.CharField(unique=True,max_length=255, null=False)
    email = models.EmailField(unique=True,max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    last_login = models.DateTimeField(auto_now_add=True, null=False)
    password = models.CharField(max_length=50,null=False)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)     
        super().save(*args, **kwargs) # Call the real save() method
    
    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)  
    
    def __str__(self) -> str:
        return f"Name: {self.username} , Email : {self.email}"
    
class URL(models.Model):
    alias = models.CharField(primary_key=True,unique=True,null=False, max_length=255, blank=False)
    long = models.URLField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    expires_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_visited = models.DateTimeField(default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def clean_alias(self):
        self.alias = self.alias.lstrip().rstrip()
        self.alias = sub(r'\s+', '-', self.alias)
    
    def save(self,*args,**kwargs):
        self.clean_alias()
        super().save(*args, **kwargs)
        