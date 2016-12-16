"""
WSGI config for theRealHaktorUnchained project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys


root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0,root)

activate_this = os.path.join(root, 'hacktorenv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "theRealHaktorUnchained.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
