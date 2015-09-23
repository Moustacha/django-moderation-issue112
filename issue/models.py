from django.db import models


# Create your models here.

class MyModel(models.Model):
    a = models.CharField(max_length=4000)
    # b = models.CharField(max_length=400, null=True,blank=True)
    c = models.IntegerField(null=True)
