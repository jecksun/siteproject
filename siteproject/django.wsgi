import os, sys

sys.path.append('/web/siteproject')

os.environ['DJANGO_SETTINGS_MODULE'] = 'siteproject.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
