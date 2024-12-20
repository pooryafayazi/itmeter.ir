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

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

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

# Summernote "
X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
                    'iframe': True,
                    'summernote': {
                    'airMode': False,
                    'width': '1200',
                    'height': '480',
                    'toolbar': [['style', ['style']],
                                ['font', ['bold', 'underline', 'clear']],
                                ['fontname', ['fontname']],
                                ['color', ['color']],
                                ['para', ['ul', 'ol', 'paragraph']],
                                ['table', ['table']],
                                ['insert', ['link', 'picture', 'video']],
                                ['view', ['fullscreen', 'codeview', 'help']],
                                ]
                        }
                    }



X_FRAME_OPTIONS = "SAMEORIGIN"