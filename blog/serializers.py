from rest_framework import serializers
from .models import Entry, Action, Category

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		fields = 'title'
		model = Category

	def to_representation(self, obj):
		return obj.title


class ActionSerializer(serializers.ModelSerializer):

	class Meta:
		fields = '__all__'
		model = Action

class EntrySerializer(serializers.ModelSerializer):

	actions = ActionSerializer(many = True, read_only = True)
	categories = CategorySerializer(many = True, read_only = True)

	class Meta:

		model = Entry
		fields = '__all__'

