from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
		gender_choices = [
						    ('0','male'),
						    ('1','female'),
						    ('2','others'),
						  ]
		gender = models.CharField(max_length=6,choices=gender_choices,default='0')
		uname=models.CharField(max_length=20)
		phone_no=models.CharField(max_length=10)
		password=models.CharField(max_length=200)
		
class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address