import json

from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from movies.permissions import SeriesPermissions

from .serializers import EntrySerializer

from .models import Entry

# Create your views here.


class EntriesModelViewSet(ModelViewSet):

	queryset = Entry.objects.all()
	serializer_class = EntrySerializer

	permission_classes = [
		SeriesPermissions
	]

	lookup_field = 'title'
	lookup_url_kwarg = 'title'

	@action(methods = ('get',), detail = True, url_path = 'content', url_name = 'content')
	def content(self, request, title):

		entry = Entry.objects.get(title = title)

		content = dict(title = entry.title, content = entry.content)

		return Response(content)





