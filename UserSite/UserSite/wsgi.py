"""
WSGI config for UserSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/django_project/UserSite')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UserSite.settings')

application = get_wsgi_application()
