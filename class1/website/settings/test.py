from website.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_default.db3'),
    }
}


try:
    from website.settings.test_local import *
except ImportError:
    pass
