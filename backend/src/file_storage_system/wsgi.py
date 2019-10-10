import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_storage_system.settings.production') 

application = get_wsgi_application()
