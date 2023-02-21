from django.db import models

class Services(models.Model):
    name=models.CharField(max_length=100)
    icon=models.CharField(max_length=20)
    text=models.CharField(max_length=500)
