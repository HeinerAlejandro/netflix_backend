from django.db import models
from django.shortcuts import reverse as reverse_django
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

from rest_framework import reverse



# Create your models here.

def upload_image_movie(instance, file):
	return 'movies/{0}/{1}'.format(instance.name, file)

def upload_capitule(instance, file):
	return '{0}/{1}'.format(instance.season.name, file)

class DescriptionData(models.Model):

	name = models.CharField(max_length = 50, verbose_name = 'Nombre', primary_key = True)
	description = models.TextField(verbose_name = 'Descripcion')

	date = models.DateTimeField(verbose_name = 'Fecha de publicacion', auto_now_add = True)

	presentation = models.ImageField(upload_to = upload_image_movie, verbose_name = 'Portada')
	
	def __str__(self):
		return self.name

	class Meta:
		abstract = True


class Season(DescriptionData):

	serie = models.ForeignKey('Serie', verbose_name = 'Serie', on_delete = models.CASCADE, related_name = 'seasons')

	class Meta:

		verbose_name = 'Temporada'
		verbose_name_plural = 'Temporadas'

class Capitule(DescriptionData):
	
	duration = models.CharField(max_length = 5)

	capitule = models.FileField(upload_to = upload_capitule, blank = True, null = True)

	season = models.ForeignKey('Season', verbose_name = 'Temporada', on_delete = models.CASCADE, related_name = 'capitules')


	class Meta:

		verbose_name = 'Capitulo'
		verbose_name_plural = 'Capitulos'

class Serie(DescriptionData):

	has_new_histories = models.BooleanField(default = False)
	number_seasons = models.IntegerField(default = 0)

	def get_absolute_url(self):
		return ''


	class Meta:

		verbose_name = 'Serie'
		verbose_name_plural = 'Series'

@receiver(post_save, sender = Season)
def saved_season(sender, **kwargs):
	
	season_instance = kwargs.get('instance')

	if kwargs.get('created', False):
		serie = season_instance.serie
		
		serie.number_seasons += 1
		serie.has_new_histories = not not F('has_new_histories')

		serie.save()