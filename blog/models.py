from django.db import models
from django.urls import reverse
from django.utils.text import slugify 

from ckeditor.fields import RichTextField


# Create your models here.


def upload_image_blog(instance, file):
	return 'blogs/{0}/{1}'.format(instance.name, file)


class Category(models.Model):

	title = models.CharField(max_length = 45, verbose_name = 'Titulo')

	def __str__(self):
		return self.title

class Action(models.Model):

	title = models.CharField(max_length = 45, verbose_name = 'Titulo')
	link = models.URLField(verbose_name = 'enlace')

	entrie = models.ForeignKey('Entry', related_name = 'actions', related_query_name = 'entrie', on_delete = models.CASCADE)


class Entry(models.Model):

	title = models.CharField(max_length = 45, verbose_name = 'Titulo')
	slug = models.SlugField(editable = False)
	content = RichTextField()
	presentation = models.ImageField(upload_to = upload_image_blog, verbose_name = 'Portada')

	categories = models.ManyToManyField(Category, related_name = 'entries', related_query_name = 'categories', verbose_name = 'Categorias')

	date = models.DateTimeField(auto_now = True)	

	def __str__(self):

		return self.title

	def save(self, *args, **kwargs):

		valueToSlug = self.title

		self.slug = slugify(valueToSlug)

		super().save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('entry-detail', kwargs = {'slug' : self.slug})