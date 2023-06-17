import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-5+!00u54!s(&^4r4v8il$&f+he5ha5-+wa)p$!x&x^)*7i)k04"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "site_reservation",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "service_reservation.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "site_reservation", "templates", "site_reservation"),
            os.path.join(BASE_DIR, "site_reservation/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "service_reservation.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_reservation',
        'USER': 'modou',
        'PASSWORD': 'modou',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'auth_plugin': 'mysql_native_password',  # Utilisez 'mysql_native_password' au lieu de 'caching_sha2_password'
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
#MEDIA_ROOT = os.path.join(BASE_DIR, "media_suite")
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/reservation/image/media_suite')
#MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'bookingluxury.bg@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'bookingluxury.bg@gmail.com'
EMAIL_HOST_PASSWORD = 'dwgcbtjnzegdrswl'
EMAIL_USE_SSL = True
