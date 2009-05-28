import os
from django.conf.urls.defaults import *
from b3breview.products.views import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # homepage
    url(r'^$', index, name="index"),

    # specific product
    url(r'^(?P<slug>[a-zA-Z0-9])/?$', product, name="product"),
    
    # archives
    url(r'^archive/?$', archive, name="archive"),
    url(r'^archive/(\d{4})/?$', year_archive, name="year-archive"),
    url(r'^archive/(\d{4})/(\d{2})/?$', month_archive, name="month-archive"),
    url(r'^archive/(\d{4})/(\d{2})/(\d+)/?$', day_archive, name="day-archive"),
    
    # Comments
    url(r'^comments/', include('django.contrib.comments.urls')),

    # Admin
    url(r'^admin/(.*)', admin.site.root),
)

# For serving static media files (css, js, images)
if settings.DEBUG:	
	urlpatterns += patterns('',
        (r'^content/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'content')}),
    )

