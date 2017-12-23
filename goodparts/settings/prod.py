from .base import *
import os
from django.core.exceptions import ImproperlyConfigured


try:
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASSWD = os.environ['DB_PASSWD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']
    BASE_URL = os.environ['BASE_URL']
    DEBUG = os.environ['DEBUG']
    SECRET_KEY = os.environ['SECRET_KEY']
    STATIC_URL = os.environ['STATIC_URL']
except KeyError:
    raise ImproperlyConfigured

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}
