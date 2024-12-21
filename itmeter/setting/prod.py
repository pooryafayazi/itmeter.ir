from itmeter.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&82z_0+)t(u*g0sl9x_%ka#_jl3_1hilg@m(##xw33i&)x-_lu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#INSTALLED_APPS = []


# sites framwork
SITE_ID = 2

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME" : "itmeter",
        "USER" : "root",
        "PASSWORD" : "",
        "HOST" : "localhost",
        "PORT" : "",        
    }
}








STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

CSRF_COOKIE_SECURE = True 