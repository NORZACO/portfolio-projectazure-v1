"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# AZURE
# from whitenoise import WhiteNoise

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
# Check for the WEBSITE_HOSTNAME environment variable to see if we are running in Azure Ap Service
# If so, then load the settings from production.py
settings_module = 'portfolio.production' if 'WEBSITE_HOSTNAME' in os.environ else 'portfolio.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
