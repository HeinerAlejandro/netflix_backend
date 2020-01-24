from django.contrib import admin
from django.utils.html import format_html

from .models import Serie, Season, Capitule
# Register your models here.

def image_presentation(obj):

		html = """
			<img 
				style = 'width : 50px;' 
			    src = '{0}'
			>
		"""
		return format_html(html, obj.presentation.url)

image_presentation.short_description = 'portada'

class SeasonInline(admin.StackedInline):
	model = Season
	extra = 1
	classes = ('collapse',)
	min_num = 0
	view_on_site = True


@admin.register(Serie)

class SerieModelAdmin(admin.ModelAdmin):

	inlines = [
		SeasonInline
	]

	list_display = (image_presentation, 'name', 'number_seasons', 'has_new_histories', 'date')
	list_display_links = ('name',)
	readonly_fields = ('has_new_histories', 'number_seasons', 'date')
	date_hierarchy = 'date'
	search_fields = ('name', )

	

	def view_on_site(self, obj):
		return obj.get_absolute_url()

	def register_season(self, obj):
		return obj.name

	register_season.empty_value_display = '???'



class CapituleInline(admin.StackedInline):
	model = Capitule
	extra = 1
	classes = ('collapse',)
	min_num = 0


@admin.register(Season)
class SeasonModelAdmin(admin.ModelAdmin):

	inlines = [
		CapituleInline
	]

	list_display = (image_presentation, 'name', 'serie','date')

admin.site.register(Capitule)
