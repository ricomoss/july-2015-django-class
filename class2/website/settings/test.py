from website.settings.base import *

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'test_default.db3'),
}


try:
    from website.settings.dev_local import *
except ImportError:
    pass
