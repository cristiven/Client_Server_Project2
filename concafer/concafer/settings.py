"""
Django settings for concafer project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import random
import string
import dj_database_url
    



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#SECRET_KEY = 'n5e06jltg@_*hfoe+h2)9s50vbvhld@c!palr16p6byi4gsuqd'
#SECRET_KEY = os.environ.get("SECRET_KEY", "".join(random.choice(string.printable) for i in range(40)))


# SECURITY WARNING: don't run with debug turned on in production!
# si debug es True estamos en desarrollo de lo contrario estamos en produccion
#DEBUG = True
#DEBUG = os.environ.get("DEBUG", False)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = os.environ.get("SECRET_KEY", "".join(random.choice(string.printable) for i in range(40)))
DEBUG = os.environ.get("DEBUG", False)


ALLOWED_HOSTS = [*]


#para envio de emails
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'concafer172@gmail.com'
EMAIL_HOST_PASSWORD = 'concafer271'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'crispy_forms',
    'registration', 
    'channels',
    'sgc',
    'chat',
    #'gdstorage',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'social_auth.backend.pipeline.social.social_auth_user',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'concafer.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #se crea el template con os.path.join(BASE_DIR, ...) que indica la direccion raiz del proyecto
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'debug':DEBUG,
        },
    },
]

WSGI_APPLICATION = 'concafer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

'''
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgresql-aerodynamic-75732',
        'USER': 'concafer_admin',
        'PASSWORD': 'admin123',
        'HOST': 'concafer.herokuapp.com',                      
        'PORT': '5432',
    }

}
'''

'''
DATABASES = {
  'default': dj_database_url.config(default="postgres://concafer_admin:admin123@concafer.herokuapp.com:5432/postgresql-aerodynamic-75732", conn_max_age=500)
}
'''

DATABASES = {
    'default': dj_database_url.config(default="postgres:///concafer", conn_max_age=500)
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#capa de canal

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "ROUTING": "chat.routing.channel_routing",
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)




SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '534423398729-264vb2bsvoj9lq31gulvrgo9m3sci9m9.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'TD3BaDNcjfuenHGF4ai2z7HJ'

SOCIAL_AUTH_FACEBOOK_KEY = '114121485934938'
SOCIAL_AUTH_FACEBOOK_SECRET = '1bb917e4aed1d3024ea6e3b0f4f98d3a'
 


#GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = os.path.join(BASE_DIR, "gdstorage.json")
#GOOGLE_DRIVE_STORAGE_SERVICE_EMAIL = '61034839021-r18v4c9k072dud32iook8pv8meaie8vv@developer.gserviceaccount.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

#configuracion de los archivos estaticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_pro", "static"),
    #'/var/www/static/',
]

# Es en donde se van a enviar los archivos estaricos que viven en STATICFILES_DIRS
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_env_concafer", "static_root")

# Son los archivos estaticos subidos por un tercero que son imagenes que son subidos por usuarios
STATIC_MEDIA = os.path.join(os.path.dirname(BASE_DIR), "static_env_concafer", "media_root") 



ACCOUNT_ACTIVATION_DAYS  =  7  # Ventana de activacion de una semana; usted puede, por supuesto, utilizar un valor diferente.
REGISTRATION_AUTO_LOGIN  =  True  # Registrar automaticamente el usuario en.
SITE_ID = 1 # Para activar la aplicacion de sites
LOGIN_REDIRECT_URL = '/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        },
        'chat': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}