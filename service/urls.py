from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import ServiceViewSet

router = SimpleRouter()

router.register('services', ServiceViewSet)

services_url = ( 
	[
		path('', include(router.urls))
	],
	'services'
)