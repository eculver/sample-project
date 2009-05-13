import os
from django.conf.urls.defaults import *
from b3breview.products.views import latest, archive
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Acts as homepage
    (r'^$', latest),

	(r'^archive/$', archive),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

# For serving static media files (css, js, images)
if settings.DEBUG:	
	urlpatterns += patterns('',
        (r'^content/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'content')}),
    )

