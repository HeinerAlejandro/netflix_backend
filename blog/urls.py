from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import EntriesModelViewSet

router = SimpleRouter()

router.register('entries', EntriesModelViewSet)

blog_urls = (
	[
		path('', include(router.urls))
	],
	'entries'
)