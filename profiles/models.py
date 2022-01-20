from django.contrib.auth import login
from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField

# Model class for Mvtel ServiceDesk profile users

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    position = models.CharField(max_length=200)
    Sdktype = models.IntegerField(blank=True)
    picture = models.ImageField(upload_to='profiles/pictures', default = 'Picture')
    last_logout = models.DateTimeField(blank=True,null=True)
    login = BooleanField(blank=True,null=True)

