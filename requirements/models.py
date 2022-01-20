from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


# Project Model

class Service(models.Model):

    project         = models.ForeignKey(Project, on_delete=models.CASCADE)
    responsable     = models.ForeignKey(User, on_delete=models.CASCADE)
    description     = models.TextField()
    created         = models.DateTimeField(auto_now_add=True)
    registerDate    = models.DateField(auto_now_add=False)
    petitioner      = models.CharField(max_length=350)
    petitionerMail  = models.EmailField()
    petitionerPhone = models.CharField(max_length=20)


def __str__(self):
    return self.projectName

