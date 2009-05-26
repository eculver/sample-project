"""
A filter to resize a ImageField on demand

Author: michelts <http://www.djangosnippets.org/users/michelts/>
URL: http://www.djangosnippets.org/snippets/192/
"""

import os
import Image
from django.template import Library
from django.conf import settings

register = Library()

def thumbnail(file, size='200x200'):
    # make sure file is a string
    file = str(file)
    
    # defining the size
    x, y = [int(x) for x in size.split('x')]
    
    # defining the filename and the miniature filename
    basename, format = file.rsplit('.', 1)
    miniature = basename + '_' + size + '.' +  format
    miniature_filename = os.path.join(settings.MEDIA_ROOT, miniature)
    miniature_url = os.path.join(settings.MEDIA_URL, miniature)
    
    # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename):
        print '>>> debug: resizing the image to the format %s!' % size
        filename = os.path.join(settings.MEDIA_ROOT, file)
        image = Image.open(filename)
        image.thumbnail([x, y]) # generate a 200x200 thumbnail
        image.save(miniature_filename, image.format)
    return miniature_url

register.filter(thumbnail)
