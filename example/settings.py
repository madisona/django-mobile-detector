# Django settings for example project.

import sys
from os.path import dirname, abspath, join
parent = abspath(join(dirname(__file__), '..'))
grandparent = abspath(join(parent, '..'))
for path in (parent, grandparent):
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