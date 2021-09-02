

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Employe(models.Model):
    # ROLE=(('respo'),('emp'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # role=models.CharField(max_length=20,choices=ROLE)


class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    responsable = models.ForeignKey(
        "Employe", on_delete=models.CASCADE, default='')


class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, default='')
