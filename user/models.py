from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms



class User(AbstractUser):
    about_me = models.TextField(null=True, blank=True)
    birth_data = models.DateField(null=True, blank=True)
    educations = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)