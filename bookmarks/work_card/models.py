from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class WorkCard(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=40)
    worker = models.ForeignKey(User.get_username)
    annotation = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    score = models.DecimalField(max_digits=4, decimal_places=2)


def __int__(self):

    return self.date

