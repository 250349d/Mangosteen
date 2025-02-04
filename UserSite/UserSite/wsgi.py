"""
WSGI config for MangTosa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/django_project/MangTosa')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MangTosa.settings')

application = get_wsgi_application()
