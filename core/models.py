from django.db import models

# Create your models here.

def upload_image_logo(instance, filename):

	return 'general/{0}'.format(filename)


class LogoEnterprise(models.Model):

	logo = models.ImageField(upload_to = upload_image_logo)

	date = models.DateTimeField(auto_now = True)