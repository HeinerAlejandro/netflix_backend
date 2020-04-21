from rest_framework import serializers
from .models import Serie, Season, Capitule

class CapituleSerializer(serializers.ModelSerializer):

	class Meta:

		model = Capitule
		fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):


	capitules = CapituleSerializer(many = True)

	class Meta:

		model = Season
		exclude = ('serie',)

class SerieSerializer(serializers.HyperlinkedModelSerializer):
	

	seasons = serializers.HyperlinkedIdentityField(
		view_name = 'movies:serie-list-seasons',
		lookup_field = 'name'
	)


	class Meta:

		model = Serie

		fields = (
			'name',
			'description',
			'date',
			'presentation',
			'has_new_histories',
			'number_seasons',
			'seasons'
		)