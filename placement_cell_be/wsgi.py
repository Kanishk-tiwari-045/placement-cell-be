import os
from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE directly
os.environ['DJANGO_SETTINGS_MODULE'] = 'placement_cell_be.settings'

application = get_wsgi_application()
