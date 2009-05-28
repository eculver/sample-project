from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField()
    primary_image = models.ImageField(upload_to="content/images/products/%Y/%m/%d", null=False)
    slug = models.SlugField(max_length=255)
    posted_by = models.ForeignKey(User)
    published = models.BooleanField(default=True, null=False)
    publish_on = models.DateTimeField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
        
    def __unicode__(self):
        return self.title	

