from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import F

def saved_season(sender, **kwargs):
	
	season_instance = kwargs.get('instance')

	if kwargs.get('created', False):
		serie = season_instance.serie
		
		serie.number_seasons += 1
		serie.has_new_histories = not not F('has_new_histories')

		serie.save()
