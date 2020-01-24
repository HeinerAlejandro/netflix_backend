from django.contrib import admin
from .models import Entry, Action, Category
# Register your models here.

class StackedAction(admin.StackedInline):

	model = Action
	extra = 3


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

	inlines = [
		StackedAction
	]


admin.site.register(Category)