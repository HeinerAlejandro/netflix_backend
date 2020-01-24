from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from .models import Serie, Season, Capitule
from .serializers import SerieSerializer, SeasonSerializer, CapituleSerializer

from .permissions import SeriesPermissions
# Create your views here.

class CapituleMovieViewSet(ModelViewSet):

	queryset = Capitule.objects.all()
	serializer_class = CapituleSerializer


class SeasonMovieViewSet(ModelViewSet):

	queryset = Season.objects.all()
	serializer_class = SeasonSerializer

	lookup_url_kwarg = 'name'
	lookup_field = 'name'

class SeriesMovieViewSet(ModelViewSet):

	queryset = Serie.objects.all()
	serializer_class = SerieSerializer
	
	permissions = [
		SeriesPermissions
	]

