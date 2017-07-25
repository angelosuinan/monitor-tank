from __future__ import unicode_literals
from django.db import models
from core.models import Base


class Suscriber(Base):
    subscriber_number = models.CharField(max_length=11)
    access_token = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=50)


class Report(Base):
    context = models.TextField(max_length=50)
    pH_level = models.FloatField(max_length=10, null=True, blank=True)
    oxygen_level = models.FloatField(max_length=10, null=True, blank=True)
    temperature_level = models.FloatField(max_length=10, null=True, blank=True)
    water_level = models.CharField(max_length=20, null=True, blank=True)
