from django.db import models
from profiles.models import Profile

# Project Model

class Project(models.Model):
    projectName = models.CharField(max_length=250)
    country     = models.IntegerField()
    active      = models.IntegerField()
    logo        = models.ImageField(upload_to='pro/pictures', default = 'Picture')

def __str__(self):
    return self.id




class ProjectForProfile(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


def __str__(self):
    return self.id