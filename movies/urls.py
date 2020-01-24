from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import SeriesMovieViewSet, SeasonMovieViewSet, CapituleMovieViewSet

router = SimpleRouter()

router.register('series', SeriesMovieViewSet)
router.register('seasons', SeasonMovieViewSet)
router.register('capitules', CapituleMovieViewSet)

movies_url = ( 
	[
		path('', include(router.urls))
	],
	'movies'
)