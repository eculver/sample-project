from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/Users/eculver/django/projects/b3breview/media/images/products')

class Product(models.Model):
	name = models.CharField(max_length=50) 
	description = models.TextField()
	primary_image = models.ImageField(upload_to="media/images/products/", storage=fs, null=False)
	slug = models.SlugField(max_length=50)
	posted_by = models.ForeignKey(User)
	timestamp = models.DateTimeField()

	def __str__(self):
		return self.name
