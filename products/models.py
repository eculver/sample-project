from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=50) 
	description = models.TextField()
	primary_image = models.ImageField(upload_to="content/images/products/%Y/%m/%d", null=False)
	slug = models.SlugField(max_length=50)
	posted_by = models.ForeignKey(User)
	timestamp = models.DateTimeField()

	def __unicode__(self):
		return self.name	

