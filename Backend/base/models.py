from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User) # should include username, uid, and pw
    # Might need gc_auth
    preferred_start = models.DateTimeField()
    preferred_end = models.DateTimeField()


class Task(models.Model):
    user = models.ForeignKey(User) # each task is related to a user
    name = models.CharField(max_length=100)
    length = models.IntegerField(max_length=24) # in hours

    # these are allowed to be blank (until algorithm runs)
    start = models.DateTimeField(Blank=True) 
    end = models.DateTimeField(Blank=True)