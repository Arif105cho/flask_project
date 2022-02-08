from django.db import models

# Create your models here.

class SignUp(models.Model):
    username=models.CharField(max_length=20)
    full_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Login(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email

