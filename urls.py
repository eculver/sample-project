from django.conf.urls.defaults import *
from b3breview.products.views import latest, archive
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Acts as homepage
    (r'^$', latest),

	(r'^archive/$', archive),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
