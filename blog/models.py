from django.db import models
from django.urls import reverse
from django.utils.text import slugify 
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

from ckeditor.fields import RichTextField


# Create your models here.


def upload_image_blog(instance, file):
	return 'blogs/{0}/{1}'.format(slugify(instance.title), file)


class Category(models.Model):

	title = models.CharField(max_length = 45, verbose_name = 'Titulo')

	class Meta:
		verbose_name = 'Categoria'

	def __str__(self):
		return self.title

class Action(models.Model):

	title = models.CharField(max_length = 45, verbose_name = 'Titulo')
	link = models.URLField(verbose_name = 'enlace')

	entries = models.ForeignKey('Entry', related_name = 'actions', related_query_name = 'entrie', on_delete = models.CASCADE)

	class Meta:

		verbose_name = 'Accion'
		verbose_name_plural = 'Acciones'

class Entry(models.Model):

	title = models.CharField(max_length = 45, verbose_name = 'Titulo')
	short_description = models.CharField(max_length = 400, verbose_name = 'Descripcion corta')
	content = RichTextField()
	
	presentation = models.ImageField(upload_to = upload_image_blog, verbose_name = 'Portada')

	categories = models.ManyToManyField(Category, related_name = 'entries', related_query_name = 'categories', verbose_name = 'Categorias')

	date = models.DateTimeField(auto_now = True)	

	def __str__(self):

		return self.title

	def get_absolute_url(self):
		return reverse('entry-detail', kwargs = {'slug' : self.slug})

	class Meta:
		verbose_name = 'Entrada'
	
@receiver(post_save, sender = Entry)
def create_default_action(sender, **kwargs):

	entry_instance = kwargs.get('instance')

	if kwargs.get('created', False):
		
		link = reverse('entries:entry-content', kwargs = dict(title = entry_instance.title))

		action = Action(
			title = 'LEER MAS',
			link = link
		)

		action.entries = entry_instance
		action.save()