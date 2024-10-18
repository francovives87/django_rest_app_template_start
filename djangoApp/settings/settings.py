import os
from pathlib import Path
from decouple import config, Csv
from datetime import timedelta

# Construir rutas dentro del proyecto como BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY desde el archivo .env
SECRET_KEY = config('SECRET_KEY')

# DEBUG: En desarrollo es True, en producción es False
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS: Diferentes por entorno
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

AUTH_USER_MODEL = 'users.CustomUser'



# CORS configuración desde el entorno
CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', default=False, cast=bool)

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='', cast=Csv())

# Añadir dominios permitidos para las solicitudes CSRF
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='', cast=Csv())

# Configuración de archivos estáticos (CSS, JS)
STATIC_URL = '/static/'  # URL para acceder a los archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directorio donde se colectan los archivos estáticos

# MEDIA_URL y MEDIA_ROOT fijos
MEDIA_URL = '/media/'  # La URL base para acceder a los archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Carpeta donde se almacenarán los archivos subidos

print(f"STATIC_ROOT: {STATIC_ROOT}")
print(f"MEDIA_ROOT: {MEDIA_ROOT}")

# Definir aplicaciones comunes
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # CORS
    # Tus apps aquí
    'apps.users',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
]

# Definir middleware común
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Middleware de CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Definir URLs y aplicaciones WSGI comunes
ROOT_URLCONF = 'djangoApp.urls'

WSGI_APPLICATION = 'djangoApp.wsgi.application'


# REST FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Configuración de JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}



# Definir configuraciones de templates comunes
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Configuración de la base de datos con variables del entorno
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Definir validadores de contraseñas comunes
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

# Configuración de internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = config('TIME_ZONE', default='UTC')
USE_I18N = True
USE_TZ = True

# Tipo de campo de clave primaria predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de correo electrónico desde .env
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Seguridad adicional para producción
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)
