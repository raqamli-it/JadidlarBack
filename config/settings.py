"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

from corsheaders.defaults import default_headers
from django.utils.translation import gettext_lazy as _
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h0p&3so%)!_=1n3mi0+a$$!162ru92^xh65l2l4nz^jy^x=&-*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',

    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    "modeltranslation",
    'corsheaders',
    'django_filters',

    'api',
    'foydali_havolalar',
    'hikmatli_sozlar',
    'hujjatlar',
    'ishtirokchilar',
    'jadidlar',
    'manbalar',
    'sahifalar',
    'slayder',
    'tadbirlar',
    'tanlovlar',
    'users',
    "authentication",

]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend'),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 15

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    # Other configurations...
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jadid_db',
        'USER': 'jadidlar_user',
        'PASSWORD': 'jadidlar_password',
        'HOST': '93.188.84.132',
        #        'HOST': 'jadid_db',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'uz'

LANGUAGES = (
    ('ru', _('Russian')),
    ('uz', _('Uzbek')),
    ('en', _('English')),
)

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/staticfiles/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [BASE_DIR / 'static', ]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

JAZZMIN_SETTINGS = {
    "site_title": "Foydali Havolalar",
    "site_brand": "Fanlar Akademiyasi",
    "site_logo": "jadid.jpg",
    "welcome_sign": "Xush Kelibsiz",
    "copyright": "Jadidlar",
    # "search_model": ["app.model_name"],

    "topmenu_links": [
        {"model": "auth.User"},
        # {"model": "auth.Group"},

        # {"name": "Foydali Havolalar", "url": "foydali_havolalar"},
        # {"name": "Hikmatli Sozlar", "url": "hikmatli_sozlar"},
        # {"name": "Hujjatlar", "url": "hujjatlar"},
        # {"name": "Ishtirokchilar", "url": "ishtirokchilar"},
        # {"name": "Jadidlar", "url": "jadidlar"},
        # {"name": "Manbalar", "url": "manbalar"},
        # {"name": "Sahifalar", "url": "sahifalar"},
        # {"name": "Slayder", "url": "slayder"},
        # {"name": "Tadbirlar", "url": "tadbirlar"},
        # {"name": "Tanlovlar", "url": "tanlovlar"},
    ],

    "navigation_expanded": False,

    "hide_apps": ['auth'],

    "show_ui_builder": True,

    "changeform_format": "collapsible",

    # "usermenu_links": [
    # {"name": "Profile", "url": "profile"},
    # {"name": "Logout", "url": "logout"},
    # {"name": "Login", "url": "login"},
    # {"name": "Signup", "url": "signup"},

    #     ]

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}

AUTH_USER_MODEL = 'users.CustomUser'
# AUTH_USER_MODEL = 'authentication.User'


LOGIN_REDIRECT_URL = '/admin/'

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

...
# Google OAuth2 settings
BASE_FRONTEND_URL = os.environ.get('DJANGO_BASE_FRONTEND_URL', default='http://127.0.0.1:8000/')
GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_HEADERS = list(default_headers) + [
    'language-code',
]

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:5300', "https://jadidlar.uz",
                        "https://backend.jadidlar.uz",]
CORS_ALLOWED_ORIGINS = [
    "https://jadidlar.uz",
    "https://backend.jadidlar.uz",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
