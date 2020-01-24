from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from movies.permissions import SeriesPermissions

from .serializers import EntrieSerializer

from .models import Entry
# Create your views here.


class EntriesModelViewSet(ModelViewSet):


	queryset = Entry.objects.all()
	serializer_class = EntrieSerializer
	permission_classes = [
		SeriesPermissions
	]

	lookup_field = 'title'
