from django.db import models

class NavigationItem(models.Model):
	title = models.CharField(max_length=50) 
	path = models.CharField(max_length=50)
	active = False
	
	def __str__(self):
		return '%s (%s)' % (self.title, self.path)
	
class FooterItem(models.Model):
	title = models.CharField(max_length=50)
	path = models.CharField(max_length=50)

	def __str__(self):
		return '%s (%s)' % (self.title, self.path)
	
