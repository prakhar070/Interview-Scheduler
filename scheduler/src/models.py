from django.db import models
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import 	User
import datetime

#Django models associated with the application

#Django model for an interview
class Interview(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField(default = datetime.datetime.now())
    end = models.DateTimeField(default = datetime.datetime.now())
    candidates = models.ManyToManyField(to='Candidate',related_name='candidates')

   
#Django model for a candidate
class Candidate(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length = 254)