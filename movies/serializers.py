from rest_framework import serializers
from .models import Serie, Season, Capitule

class CapituleSerializer(serializers.ModelSerializer):

	class Meta:

		model = Capitule
		fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):


	capitules = serializers.HyperlinkedRelatedField(
		view_name = 'movies:capitule-detail',
		many = True,
		read_only = True,
	)

	class Meta:

		model = Season
		exclude = ('serie',)

class SerieSerializer(serializers.HyperlinkedModelSerializer):
	

	seasons = serializers.HyperlinkedRelatedField(
		view_name = 'movies:season-detail',
		many = True,
		read_only = True,
		lookup_field = 'name'
	)


	class Meta:

		model = Serie

		fields = (
			'id',
			'name',
			'description',
			'date',
			'presentation',
			'has_new_histories',
			'number_seasons',
			'seasons'
		)