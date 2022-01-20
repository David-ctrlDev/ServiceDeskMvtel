from django import forms
from django.forms.widgets import DateTimeBaseInput
from django.shortcuts import render
from projects.models import Project, ProjectForProfile

class ServiceFormPetitioner(forms.Form):
    projectsList = []
    profileProjects = (ProjectForProfile.objects.all())

    for i in profileProjects:
       
       project = Project.objects.get(pk=i.project_id)
       projectsList.append(project)

    projectList = ((f'{i.id}', f'{i.projectName}') for i in projectsList)

    project         = forms.ChoiceField(label='Proyecto',required=True, choices= projectList)
    description     = forms.CharField(label='Descripción')
    registerDate    = forms.DateField(label ='Fecha Solicitud',required=True,input_formats=['%Y-%m-%d'],widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    petitioner      = forms.CharField(max_length=350, required=True, label= 'Contacto')
    petitionerMail  = forms.EmailField(required=True, label='Email Contacto')
    petitionerPhone = forms.CharField(max_length=20,required=True, label='Teléfono Contacto')
    campus          = forms.CharField(required=True, label='Sede',max_length=350)

