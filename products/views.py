from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Product

def latest(request):
    template_vars = {}
    template_vars["products"] = products = Product.objects.all()
    return render_to_response("product.html", template_vars, context_instance=RequestContext(request))

def archive(request):
    # grab a subset of products 
    
    # plop it out to view
    return render_to_response("archive.html", context_instance=RequestContext(request))