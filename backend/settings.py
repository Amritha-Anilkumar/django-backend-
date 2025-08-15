import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xt$2+=2c9xm!#-&hts^an5w(==&l=b4%4jxj@qm95y6#x=0td%'

DEBUG = True

ALLOWED_HOSTS = [
    "django-backend-7.onrender.com",
    "127.0.0.1",
    "localhost",
]

# -------------------- INSTALLED APPS --------------------
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'corsheaders',
    'rest_framework',

    # Local apps
    'mainapp',
]

# -------------------- MIDDLEWARE --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # CORS middleware should be placed as high as possible
    'corsheaders.middleware.CorsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------- CORS & CSRF --------------------
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
     # Old frontend
    "https://inspiring-tarsier-943031.netlify.app",
     "https://astounding-klepon-6a36cd.netlify.app" # Current frontend
    "http://localhost:3000",                        # Local dev
]

CSRF_TRUSTED_ORIGINS = [
    "https://prismatic-otter-804c65.netlify.app",
    "https://inspiring-tarsier-943031.netlify.app",
    "https://astounding-klepon-6a36cd.netlify.app"
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# -------------------- DATABASE CONFIG --------------------
if os.environ.get('RENDER'):
    DATABASES = {
        'default': dj_database_url.config(
            default='postgresql://vyasayoga_user:BnaPsnMcTYkq9TtI3YdC5iRBVRznj5gj@dpg-d2cql79r0fns73e6t36g-a/vyasayoga'
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'vyasayoga',
            'USER': 'root',
            'PASSWORD': 'Root',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

# -------------------- PASSWORD VALIDATION --------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------- INTERNATIONALIZATION --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------- STATIC & MEDIA FILES --------------------
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------- EMAIL CONFIG --------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vyasayogacenter@gmail.com'
EMAIL_HOST_PASSWORD = 'hzoc dpdm sivx kwfp'
