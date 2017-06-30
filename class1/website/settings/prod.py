from website.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'website_db_name',
        'USER': 'website_db_user',
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


try:
    from website.settings.prod_local import *
except ImportError:
    pass
