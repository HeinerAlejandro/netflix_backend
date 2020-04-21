from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Service
from .serializer import ServiceSerializer

# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):

	serializer_class = ServiceSerializer
	queryset = Service.objects.all()

	@action(methods = ['get'], detail = True)
	def get_budget(self, pk):

		service = Service.objects.get(pk = pk).values()

		return Response(service)
		