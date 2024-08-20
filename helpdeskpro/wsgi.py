"""
WSGI config for helpdeskpro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from utils import utils
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpdeskpro.settings')

application = get_wsgi_application()

utils.check_tickets_on_db()
