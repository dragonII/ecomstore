"""
Django settings for ecomstore project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Change to true before deploying into production
ENABLE_SSL = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!bv71rcm=+heuyg%!qk=#yv!uyenvv^w=h$jk+g^rh!#4@i5(^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'catalog',
    'utils',
    'cart',
    'checkout',
    'accounts',
    'search',
    #'djangodblog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'SSLMiddleware.SSLRedirect',
    #'djangodblog.DBLogMiddleware',
)

ROOT_URLCONF = 'ecomstore.urls'

WSGI_APPLICATION = 'ecomstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'lwang',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',	
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        )

TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
        )

SITE_NAME = 'Modern Musician'
SITE_ID = 1
META_KEYWORDS = 'Music, instruments, music accessories, musician supplies'
META_DESCRIPTION = 'Modern Musician is an online supplier of instruments, sheet music, and other accessories for musicians'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'utils.context_processors.ecomstore',
        )


GOOGLE_CHECKOUT_MERCHANT_ID = 'abcdefg4TestPurpose'
GOOGLE_CHECKOUT_MERCHANT_KEY = 'key4TestPurpose'
GOOGLE_CHECKOUT_URL = 'https://sandbox.google.com/checkout/api/v2/merchantCheckout/Merchant/' + GOOGLE_CHECKOUT_MERCHANT_ID

AUTHNET_POST_URL = 'test.authorize.net'
AUTHNET_POST_PATH = '/gateway/transact.dll'
AUTHNET_LOGIN = 'wanglong1982'
AUTHNET_API_LOGIN_ID = '5g9cT5NBRns'
AUTHNET_KEY = '3Qz22x5HLPm8P2W4'


LOGIN_REDIRECT_URL = '/accounts/my_account/'

AUTH_PROFILE_MODULE = 'accounts.userprofile'
#AUTH_USER_MODEL = 'accounts.UserProfile'

PRODUCTS_PER_PAGE = 12
