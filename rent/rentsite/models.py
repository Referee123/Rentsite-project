from django.db import models


# Create your models here.
class Apartament(models.Model):
    title = models.TextField(max_length=100, unique=True)
    image = models.TextField(max_length=750, blank=True, null=True)
    address = models.TextField(max_length=100, unique=True, null=True)
    description = models.CharField(max_length=250, blank=True, null= True)
    availlability = models.BooleanField(default=None)
    start_reservation = models.DateTimeField(max_length= 30, auto_now=False, auto_now_add=False, unique=True, null=True)
    end_reservation = models.DateTimeField(max_length= 30, auto_now=False, auto_now_add=False, unique=True, null=True)