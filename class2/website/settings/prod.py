from website.settings.base import *

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'website_db_name',
        'USER': 'website_db_user',
    }
}


try:
    from website.settings.prod_local import *
except ImportError:
    pass
