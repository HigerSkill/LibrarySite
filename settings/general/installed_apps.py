# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
]

SIDE_PACKAGES_APPS = [
    'django_extensions',
]

CUSTOM_APPS = [
    'apps.authors',
    'apps.books',
    'apps.subscribers',
]

INSTALLED_APPS += SIDE_PACKAGES_APPS + CUSTOM_APPS
