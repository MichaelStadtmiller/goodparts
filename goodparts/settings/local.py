from .base import *
from django.core.exceptions import ImproperlyConfigured


try:
    DB_NAME = 'goodparts'
    DB_USER = 'goodparts'
    DB_PASSWD = 'goodparts'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    ALLOWED_HOSTS = ['*']
    BASE_URL = 'http://127.0.0.1:8000'
    DEBUG = True
    SECRET_KEY = 'nmhk3%5hft#n@luww6yrhwup-mx%d!hjbfy-4s&0s1$@hyjogl'
    STATIC_URL = '/static/'
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


