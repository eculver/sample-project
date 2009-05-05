from django import template
from django.conf import settings
from b3breview.common.models import NavigationItem, FooterItem

register = template.Library();

def show_navigation(context):
	request = context['request']
	navigation_items = NavigationItem.objects.all()
	navigation_items[0].active = True
	active_navigation_item = 1
	
	for navigation_item in navigation_items:
		if request.get_full_path() == navigation_item.path:
			active_navigation_item = navigation_item.id	
			navigation_item.active = True
		
	return { "navigation_items": navigation_items, "active_navigation_item": active_navigation_item }
   
register.inclusion_tag("navigation.html", takes_context=True)(show_navigation)

def show_footer_links():
	return {"footer_links": FooterItem.objects.all() }

register.inclusion_tag("footer_links.html")(show_footer_links)
		