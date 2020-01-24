from rest_framework import serializers
from .models import Entry

class EntrieSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Entry
		fields = '__all__'
		lookup_field = 'title'
		extra_kwargs = {
			'url' : { 'lookup_fiel' : 'title' }
		}

