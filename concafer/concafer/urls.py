"""concafer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from sgc import views as core_views
from .views import about
from chat import views 

urlpatterns = [
    url(r'^home/$', core_views.home, name='home'),
    url(r'^$', core_views.inicio, name='inicio'),
    url(r'^login/$', core_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', core_views.LogOut, name='LogOut'),
    url(r'^gd/$', core_views.gd, name='gd'),
    url(r'^about/$', about, name='about'),
    url(r'^empleo/$', core_views.empleado, name='empleo'),
    url(r'^cotizacion/$', core_views.cotizacion, name='cotizacion'),

    # Para utilizar todas las vistas de django-registration-redux
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^chat/$', views.chat_room, name='chat'),
    url(r'^adminrooms/$',  views.admin_chat, name='chat'),
    url(r'^chat/$',  views.about, name='chat'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]

# se coloca para asegurar que los urls estan en desarrollo

'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
