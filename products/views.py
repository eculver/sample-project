from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Product

def index(request):
    template_vars = {}
    template_vars["latest_product"] = Product.objects.filter(published=True, deleted_on=None).latest('created_on')
    return render_to_response("index.html", template_vars, context_instance=RequestContext(request))

def product(request, slug):
    template_vars = {}
    template_vars["product"] = Product.objects.filter(published=True, deleted_on=None, slug=slug)
    return render_to_response("product.html", template_vars, context_instance=RequestContext(request))

def archive(request):
    return render_to_response("archive.html", context_instance=RequestContext(request))

def year_archive(request, year):
    return render_to_response("archive.html", context_instance=RequestContext(request))
    
def month_archive(request, year, month):
    return render_to_response("archive.html", context_instance=RequestContext(request))
    
def day_archive(request, year, month, day):
    return render_to_response("archive.html", context_instance=RequestContext(request))