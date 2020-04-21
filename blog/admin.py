from django.contrib import admin
from django.utils.html import format_html

from .models import Entry, Action, Category
# Register your models here.

def categories_presentation(obj):
	
	html = """
		<select>
	"""
	if obj.categories:
		for category in obj.categories.all():
			html += "<option>" + category.title + "</option>"

	html += "</select>"

	return format_html(html)

categories_presentation.short_description = 'CATEGORIAS'

def image_presentation(obj):
	
	html = """
		<img 
			style = 'width : 50px;' 
		    src = '{0}'
		>
	"""

	return format_html(html, obj.presentation.url)

image_presentation.short_description = 'PORTADA'

class StackedAction(admin.StackedInline):

	model = Action
	extra = 3


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

	inlines = [
		StackedAction
	]

	list_display = (image_presentation, 'title', categories_presentation, 'date')


admin.site.register(Category)