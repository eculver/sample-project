from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Product

def latest(request):
	# grab the latest product
	
	# stick it into context
	
	# plop it out to view
	
	return render_to_response("product.html", context_instance=RequestContext(request))

def archive(request):
	# grab a subset of products 
	
	# plop it out to view
	return render_to_response("archive.html", context_instance=RequestContext(request))