from django.db import models

# Create your models here.

class Service(models.Model):

	description = models.CharField(max_length = 25)
	cost = models.FloatField()

