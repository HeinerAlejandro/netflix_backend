from django.urls import include, path

from .views import IndexView

core_urls = (
	[
		path('', IndexView.as_view())
	],
	'core'
)