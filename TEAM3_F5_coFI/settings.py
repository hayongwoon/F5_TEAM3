"""
Django settings for TEAM3_F5_coFI project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

# json 파일있는 관리자만 접근권한있게하기 위해 로컬 json과 연결
import json
import os
from pathlib import Path

import environ
import pymysql
import storages.backends.s3boto3
from django.core.exceptions import ImproperlyConfigured

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

# 로컬용 서버
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userapp',
    'articleapp',
    'commentapp',
    'likeapp',
    'bookmarkapp',
    'careerapp',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',

    'crispy_forms',

    'ckeditor',
    'ckeditor_uploader',


    'storages',
]

TIME_ZONE = 'Asia/Seoul'

USE_TZ = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TEAM3_F5_coFI.urls'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


### s3와 연동했다면, aws.json파일 깃 이그노어를 해놨기에 git push 할 때는 이 구간을 주석 처리해주세요!
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#
# with open(os.path.join(BASE_DIR, 'aws.json')) as f:
#     secrets = json.loads(f.read())
# AWS_ACCESS_KEY_ID = secrets['AWS']['ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = secrets['AWS']['SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = secrets['AWS']['STORAGE_BUCKET_NAME']
# AWS_DEFAULT_ACL = 'public-read' # 올린 파일을 누구나 읽을 수 있게 지정합니다!
# AWS_S3_ADDRESSING_STYLE = "virtual"
######################################################################


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

WSGI_APPLICATION = 'TEAM3_F5_coFI.wsgi.application'




DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "TEAM3",
        "USER": "root",
        "PASSWORD": "2349",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

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


USE_I18N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# 배포용
STATIC_URL = 'static/'
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "static")
]
# STATIC_ROOT = os.path.join("static")


# article_front에서옴
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'height': 300,
        'width': 800,
    }
}

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
# STATIC_ROOT = os.path.join("static")

# 로컬용 (s3에 스태틱올릴때는 아래 주석풀고 배포용 주석 걸기)
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]



# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field



AUTH_USER_MODEL = 'userapp.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',

)

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# try:
#     from TEAM3_F5_coFI.deploy_settings import *
# except ImportError:
#     pass

try:
    from TEAM3_F5_coFI.local_settings import *
except ImportError:
    pass

