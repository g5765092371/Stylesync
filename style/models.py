from django.db import models

class personstyle(models.Model):
    name = models.CharField(max_length=20)
    height = models.IntegerField()
    weight = models.IntegerField()
    setting = models.CharField(max_length=20)
    weather = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

class clothstyle(models.Model):
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    style = models.CharField(max_length=20)
    size = models.CharField(max_length=20)