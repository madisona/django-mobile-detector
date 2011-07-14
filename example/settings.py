# Django settings for example project.

# app lives in a directory above our example
# project so we need to make sure it is findable on our path.
import sys
from os.path import abspath, dirname, join
parent = abspath(dirname(__file__))
grandparent = abspath(join(parent, '..'))
for path in (grandparent, parent):
    if path not in sys.path:
        sys.path.insert(0, path)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'example.db',
    }
}

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'mobile_detector.context_processors.detect_mobile',
)

ROOT_URLCONF = 'example.urls'

INSTALLED_APPS = (
    'mobile_detector',
    'sample',
)

MOBILE_COOKIE_NAME = "use_mobile"