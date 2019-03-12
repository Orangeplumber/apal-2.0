"""
Django settings for apal project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g8)bb#ut&koz)c18*nu7o7#yp9fimjauya8_180&+en!$#jms&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.apalfresh.com', 'apalfresh.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'home',
    'shop',
    'cart',
    'orders',
    'paytm',

    'pwa',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'django.contrib.admindocs',
]
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'apal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

MEDIA_ROOT = u'/var/www/sites/apal-2.0/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, '/media')
MEDIA_URL = '/media/'
if not DEBUG:
    STATIC_ROOT =u'/var/www/sites/apal-2.0/static/'
# STATIC_ROOT = u'/var/www/sites/apal-2.0/static'
# STATIC_ROOT=os.path.join(BASE_DIR, '/static')
STATIC_URL = '/static/'

# LOGIN_REDIRECT_URL = 'product_list'
# LOGOUT_REDIRECT_URL = 'product_list'

CART_SESSION_ID = 'cart'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
EMAIL_VERIFICATION=True

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_SSL=True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = False
# EMAIL_PORT = 587
EMAIL_PORT=465
EMAIL_HOST_USER = 'harnish1198@gmail.com'
EMAIL_HOST_PASSWORD = 'Op1salone'

# EMAIL_USE_TLS = True
# EMAIL_USE_SSL=False
# EMAIL_HOST = 'smtp.zoho.com'
# EMAIL_PORT=587
# EMAIL_HOST_USER = 'support@apalfresh.com'
# EMAIL_HOST_PASSWORD = 'Op1salne!'

# paytm credentials
PAYTM_MERCHANT_KEY = "sf55c%prMEHGn@uP"
PAYTM_MERCHANT_ID = "OytXzr28687551371003"
HOST_URL = "https://www.apalfresh.com"
PAYTM_CALLBACK_URL = "/paytm/response/"

if DEBUG:
    PAYTM_MERCHANT_KEY = "sf55c%prMEHGn@uP"
    PAYTM_MERCHANT_ID = "OytXzr28687551371003"
    PAYTM_WEBSITE = 'WEB_STAGING'
    HOST_URL = 'https://www.apalfresh.com'
    '''
    In sandbox enviornment you can use following wallet credentials to login and make payment.
    Mobile Number : 7777777777
    Password : Paytm12345
    This test wallet is topped-up to a balance of 7000 Rs. every 5 minutes.
    '''


PWA_APP_NAME = 'ऐpal'
PWA_APP_DESCRIPTION = "My app description"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/images/apple.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
