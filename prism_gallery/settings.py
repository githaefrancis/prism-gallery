"""
Django settings for prism_gallery project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url
from decouple import config,Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Define the media path
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-q$l7e5z_*$4tx(z63%&6pzk8am548qtkug!@(q$!qp)i#2^ava'
MODE=config("MODE",default="dev")

SECRET_KEY=config('SECRET_KEY')
print(config)
DEBUG=os.environ.get('DEBUG',False)
print(config('DB_NAME'))
print(config('DB_USER'))
print(config('DB_PASSWORD'))
print(config('DB_HOST'))
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'images',
    'category',
    'location',
    'django_bootstrap5'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'prism_gallery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'prism_gallery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# db_name=os.environ.get("DB_NAME")
# db_user=os.environ.get("DB_USER")
# db_password=os.environ.get("PASSWORD")

# DATABASES = {
    
#     'default':{
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':db_name,
#          'USER':db_user,
#          'PASSWORD':db_password,
#     }
# }
            # 'ENGINE':'django.db.backends.postgresql_psycopg2',

if config('MODE')=="dev":
    DATABASES={

        'default':{
            'ENGINE':'django.db.backends.postgresql',
            'NAME':config('DB_NAME'),
            'USER':config('DB_USER'),
            'PASSWORD':config('DB_PASSWORD'),
            'HOST':config('DB_HOST'),
            'PORT':config('DB_PORT'),
        }
    }

else:
    DATABASES={

        'default':dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }

db_from_env=dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS=config('ALLOWED_HOSTS',cast=Csv())

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE='Africa/Nairobi'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


django_heroku.settings(locals())