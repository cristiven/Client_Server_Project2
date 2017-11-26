"""
WSGI config for concafer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "concafer.settings")
channel_layer = channels.asgi.get_channel_layer ()



#application = get_wsgi_application()
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())
