"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGOUT_REDIRECT_URL='login'
LOGIN_REDIRECT_URL='account:home'
LOGIN_URL='login'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # myapp
    'blog.apps.BlogConfig',
    'Product.apps.ProductConfig',
    'account.apps.AccountConfig',
    'cart.apps.CartConfig',
    'Product_api.apps.ProductApiConfig',
    'extentions',
    'widget_tweaks',
    'crispy_forms',
    'comment',
    'django_filters',
    # api app
    'blog_api.apps.BlogApiConfig',
    'account_api.apps.AccountApiConfig',
    # rest
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    # 'dj_rest_auth',   
    # 'allauth',
    'djoser',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'dj_rest_auth.registration',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'OPTIONS': {
#             'sql_mode': 'traditional',
#         },
#         'NAME': 'shop',
#         'USER': 'root',
# #         'PASSWORD': 'DB_PASSWORD',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'
USE_I18N = True

USE_L10N = True

USE_TZ = True
# drf
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'account_api.permissions.IsStaff',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # jwt
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # knox
        # oauth
        # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication' ,
  ],
  'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
#   'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     )

}
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}
DJOSER = {
    'LOGIN_FIELD':'email',
    'SET_USERNAME_RETYPE':True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'SEND_CONFIRMATION_EMAIL':True,
    'SET_USERNAME_RETYPE':True,
    'SET_PASSWORD_RETYPE':True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SERIALIZERS': {
        'user_create':'account_api.serializers.CreateUserSerializer',
        'user':'account_api.serializers.CreateUserSerializer',
        'current_user': 'account_api.serializers.CreateUserSerializer',
        'user_delete':'djoser.serializers.UserDeleteSerializer',
        # 'token': 'djoser.serializers.TokenSerializer',
        # 'token_create': 'djoser.serializers.TokenCreateSerializer'
    },
}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK='bootstrap4'
STATICFILES_DIRS=[BASE_DIR / 'static']
STATIC_URL = '/static/'
MEDIA_URL='/media/'
MEDIA_ROOT= BASE_DIR / 'media'
AUTH_USER_MODEL='account.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
SITE_ID=1
REST_USE_JWT=True
JWT_AUTH_COOKIE='access'
JWT_AUTH_REFRESH_COOKIE='refresh'
CORS_ORIGIN_WHITELIST=[
    'http://localhost:3000'
]