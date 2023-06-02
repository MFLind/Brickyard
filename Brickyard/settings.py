"""
Django settings for Brickyard project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages
import dj_database_url

if not os.environ.get("PRODUCTION"):
    from dotenv import load_dotenv

    load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['brickyard.herokuapp.com',
                 '8000-mflind-brickyard-oywbjfhna6q.ws-eu98.gitpod.io',
                 'www.brickyard.se', 'localhost']

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# Application definition


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_bootstrap5",
    "Brickyardshop",
    "products",
    "basket",
    "checkout",
    "profiles",
    "marketing",
    # Other
    "anymail",
    "crispy_forms",
    'crispy_bootstrap5'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #   'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Brickyard.urls"


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

CSRF_TRUSTED_ORIGINS = [
    "https://appname.herokuapp.com",
    "https://8000-mflind-brickyard-oywbjfhna6q.ws-eu98.gitpod.io",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                # required by allauth
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "basket.contexts.basket_contents",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
# EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', '')
# EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', '')
# EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN', '')
# EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')

# EMAIL_BACKEND = 'django_o365mail.EmailBackend'

# O365_MAIL_CLIENT_ID = os.getenv("EMAIL_HOST_USER", "")
# O365_MAIL_CLIENT_SECRET = os.getenv("EMAIL_HOST_PASSWORD", "")
# O365_MAIL_TENANT_ID = os.getenv("O365_MAIL_TENANT_ID", "")

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": os.environ.get('MAILGUN_API_KEY', ''),
    "MAILGUN_SENDER_DOMAIN": 'brickyard.se',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "hej@brickyard.se"  # if you don't already have this in settings
SERVER_EMAIL = "hej@brickyard.se"  # ditto (default from-email for Django errors)


ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

WSGI_APPLICATION = "Brickyard.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    #    "default": {},
    #    'prod': dj_database_url.parse(os.getenv('DATABASE_URL')),
    #    'local': dj_database_url.parse(f"sqlite:////{BASE_DIR}/db.sqlite3")
    #    'default': dj_database_url.parse(f"sqlite:////{BASE_DIR}/db.sqlite3")
    'default': dj_database_url.parse(os.getenv('DATABASE_URL')),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

DJANGO_CONTRIB_APV = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": f"{DJANGO_CONTRIB_APV}.UserAttributeSimilarityValidator",
    },
    {
        "NAME": f"{DJANGO_CONTRIB_APV}.MinimumLengthValidator",
    },
    {
        "NAME": f"{DJANGO_CONTRIB_APV}.CommonPasswordValidator",
    },
    {
        "NAME": f"{DJANGO_CONTRIB_APV}.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
DJANGO_CLOUD_SS = 'cloudinary_storage.storage'

STATIC_URL = "/static/"
if not os.environ.get("PRODUCTION"):
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    STATICFILES_DIRS = []
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_STORAGE = f'{DJANGO_CLOUD_SS}.StaticHashedCloudinaryStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
DEFAULT_FILE_STORAGE = f'{DJANGO_CLOUD_SS}.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Stripe
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = "sek"
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "")
DEFAULT_FROM_EMAIL = "hej@brickyard.se"

MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY", "")
MAILCHIMP_REGION = os.getenv("MAILCHIMP_REGION", "")
MAILCHIMP_MARKETING_AUDIENCE_ID = os.getenv("MAILCHIMP_MARKETING_AUDIENCE_ID")

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUD_NAME", ""),
    'API_KEY': os.getenv("API_KEY", ""),
    'API_SECRET': os.getenv("API_SECRET", "")
}
