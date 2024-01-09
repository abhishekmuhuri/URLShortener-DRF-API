from django.db import models
from django.contrib.auth.models import AbstractUser
from re import sub
from datetime import datetime, timedelta


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self) -> str:
        return f"Name: {self.username} , Email : {self.email}"


class URL(models.Model):
    alias: str = models.CharField(primary_key=True, unique=True, null=False, max_length=255, blank=False, db_index=True)
    long = models.URLField(null=False, blank=False)
    created_at : datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    expires_at : datetime = models.DateTimeField(blank=True, null=True)
    last_visited = models.DateTimeField(default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def clean_alias(self):
        self.alias = self.alias.lstrip().rstrip()
        self.alias = sub(r'\s+', '-', self.alias)

    def save(self, *args, **kwargs):
        self.clean_alias() 
        super().save(*args, **kwargs)
        ## TODO REPLACE THIS WITH VAR
        self.expires_at = (self.created_at + timedelta(hours=24))
        
    def __str__(self):
        return f"Alias: {self.alias}, Long: {self.long}, User: {self.user}"
