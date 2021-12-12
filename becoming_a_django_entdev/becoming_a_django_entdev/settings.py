"""
Django settings for becoming_a_django_entdev project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import posixpath
import django_heroku
import dj_database_url
import dotenv

from pathlib import Path
from django.contrib.messages import constants as messages


# Chapter 2 - Project Configuration
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chapter 2 - Project Configuration
dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Chapter 2 - Project Configuration
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# Chapter 2 - Project Configuration
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

# Chapter 2 - Project Configuration
INTERNAL_IPS = [
    '127.0.0.1',
]

# Chapter 2 - Project Configuration
ALLOWED_HOSTS = [
    # Keep these two as is, unless you are using different local/internal IP's
    '127.0.0.1',
    'localhost',
    # Add your-domain.com
    'mikedinder.com',
    'www.mikedinder.com',
    'dev.mikedinder.com',
    'staging.mikedinder.com',
    # Add your-heroku-app.herokuapp.com
    'becoming-an-entdev.herokuapp.com',
    'mighty-sea-09431.herokuapp.com',
    'pure-atoll-19670.herokuapp.com',
]

# Chapter 7 - Email Test Service Integration
if DEBUG:
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
else:
    # Production Email Connection Settings Go Here...
    pass

# Application References
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-INSTALLED_APPS
DJANGO_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', # Chapter 7 - Django Messages Framework
    'django.contrib.messages', # Chapter 7 - Django Messages Framework
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'debug_toolbar', # Introduced in Chapter 9
    'django_extensions',
    'address',
    'djmoney',
    'phone_field',
    'rest_framework', # Chapter 8 - Django REST Framework
    'rest_framework.authtoken', # Chapter 8 - Django REST Framework
]

LOCAL_APPS = [
    #'becoming_a_django_entdev.chapter_1', - Only use for chapter 1 or to go back and practice generating diagrams in that chapter, Chapter 3 - 10, this will need to be commented out in order to use those chapters without errors. You can always practice generating diagrams on other apps/models as well.
    'becoming_a_django_entdev.chapter_2',
    'becoming_a_django_entdev.chapter_3',
    'becoming_a_django_entdev.chapter_4',
    'becoming_a_django_entdev.chapter_5',
    'becoming_a_django_entdev.chapter_6',
    'becoming_a_django_entdev.chapter_7',
    'becoming_a_django_entdev.chapter_8',
]

# Chapter 2 - Project Configuration
#### MERGE ALL APPS ####
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Chapter 2 - Project Configuration
# Middleware framework
# https://docs.djangoproject.com/en/3.2/topics/http/middleware/
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Chapter 7 - Django Messages Framework
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', # Chapter 7 - Django Messages Framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Chapter 2 - Project Configuration
ROOT_URLCONF = 'becoming_a_django_entdev.urls'

# Chapter 2 - Project Configuration
# Template configuration
# https://docs.djangoproject.com/en/3.2/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages', # Chapter 7 - Django Messages Framework
                'becoming_a_django_entdev.context_processors.global_context',
            ],
        },
    },
]

# Chapter 2 - Project Configuration
WSGI_APPLICATION = 'becoming_a_django_entdev.wsgi.application'
PREPEND_WWW = False
APPEND_SLASH = True

# Chapter 2 - Project Configuration
# Database Connection that was auto-generated using the Visual Studio IDE. An SQLite Database was also auto-created in the project root directory.
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Chapter 2 - Project Configuration
# Database Connection used in Chapter 2, works with Heroku as our Host. Relies on this variable in the .env file DATABASE_URL = postgres://postgres:db_password@localhost:5432/db_name
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Chapter 3 - Django Models
# Django 3.2 Default Auto ID (Primary Key Setting)
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Chapter 2 - Project Configuration
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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

# Chapter 3 - Custom User Model
AUTH_USER_MODEL = 'chapter_3.Seller'

# Chapter 2 - Project Configuration
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Chapter 2 - Project Configuration
# Django-Money Field Package
CURRENCIES = ('USD', 'EUR')
CURRENCY_CHOICES = [
    ('USD', 'USD $'),
    ('EUR', 'EUR €'),
]

# Chapter 8 - Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.IsAdminUser',
        #'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        #'rest_framework.permissions.DjangoModelPermissions',
    ],
    #'PAGE_SIZE': 10
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

# Chapter 7 - Django Messages Framework
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
# Alternate Choices
#MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
#MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
#MESSAGE_STORAGE = 'django.contrib.messages.storage.base.BaseStorage'

# Chapter 7 - Django Messages Framework
if DEBUG:
    MESSAGE_LEVEL = messages.DEBUG
else:
    pass

# Chapter 7 - Django Messages Framework
# Custom Message Tag Constants
MINOR = 50
MAJOR = 60
CRITICAL = 70

# Chapter 7 - Django Messages Framework
MESSAGE_TAGS = {
    messages.INFO: 'information',
    MINOR: 'minor',
    MAJOR: 'major',
    CRITICAL: 'critical',
}

# Chapter 7 - Django Messages Framework
import mimetypes
mimetypes.add_type('application/javascript', '.js', True)

# Chapter 9 - Testing/Debug Tool
def show_toolbar(request):
    return True

# Chapter 9 - Testing/Debug Tool
# SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = DEBUG

# Chapter 9 - Testing/Debug Tool
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
    'INTERCEPT_REDIRECTS': False,
}

# Chapter 2 - Project Configuration
django_heroku.settings(locals())

# Chapter 2 - Project Configuration
options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)

# Chapter 2 - Project Configuration
try:
    from .local_settings import *
except ImportError:
    pass
