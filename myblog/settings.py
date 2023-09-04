

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tmiu5v8dq1jk38mtwa1l#kogz=x%8vf6s5+tdvby^@4&qo7or+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # ...
    'rest_framework.authtoken',
    'users',
    'myblog',
    'users',
    'posts',
    'comments'
    # ...
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'myblog',
    'users',
    'posts',
    'comments',
    'rest_framework_simplejwt',
]

SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'your_project.urls.swagger_info',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Время жизни access-токена (60 минут, можно изменить)
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Время жизни refresh-токена (1 день, можно изменить)
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=120),  # Время жизни sliding-токена (2 часа, можно изменить)
    'SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD': timedelta(minutes=5),  # Период, в течение которого можно обновить sliding-токен (5 минут, можно изменить)
    'SLIDING_TOKEN_REFRESH_AFTER_INACTIVITY': timedelta(hours=1),  # Период неактивности пользователя, после которого sliding-токен можно обновить (1 час, можно изменить)
    'SLIDING_TOKEN_REFRESH_SLIDING_DELTA': timedelta(minutes=30),  # Интервал обновления sliding-токена (30 минут, можно изменить)
    'SLIDING_TOKEN_REFRESH_ON_LOGIN': True,  # Обновлять sliding-токен при входе пользователя (можно изменить)
    'SLIDING_TOKEN_REFRESH_ON_REFRESH': True,  # Обновлять sliding-токен при обновлении refresh-токена (можно изменить)
    'SLIDING_TOKEN_REFRESH_ON_ACTIVATION': False,  # Обновлять sliding-токен при активации (можно изменить)
    'SLIDING_TOKEN_REFRESH_ON_PASSWORD_CHANGE': False,  # Обновлять sliding-токен при изменении пароля (можно изменить)
    'SLIDING_TOKEN_REFRESH_ON_LOGOUT': False,  # Обновлять sliding-токен при выходе (можно изменить)
    'SLIDING_TOKEN_REFRESH_ON_EMAIL_CONFIRMATION': False,  # Обновлять sliding-токен при подтверждении email (можно изменить)
    'ALGORITHM': 'HS256',  # Алгоритм шифрования (можно изменить)
    'SIGNING_KEY': 'b1232ae9d25f05b795a31df898c4e8c2434f984e3110caedd2cffec42b28a0db',
    'VERIFYING_KEY': '6dd84d1d864b79cd247062a3d503025d382fda7033228ff9ef0884024bbcd253',
    'AUTH_HEADER_TYPES': ('Bearer',),  # Тип заголовка аутентификации (можно изменить)
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),  # Классы токенов (можно изменить)
    'USER_ID_CLAIM': 'user_id',  # Ключ, используемый для хранения ID пользователя в токене (можно изменить)
    'USER_ID_FIELD': 'id',  # Поле, используемое для хранения ID пользователя (можно изменить)
    'USER_EMAIL_FIELD': 'email',  # Поле, используемое для хранения email пользователя (можно изменить)
    'UPDATE_LAST_LOGIN': True,  # Обновлять дату последнего входа пользователя (можно изменить)
    'SLIDING_TOKEN_REFRESH_RESET': True,  # Сбрасывать sliding-токен при обновлении refresh-токена (можно изменить)
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # Используйте токен-аутентификацию
    ],
}

AUTH_USER_MODEL = 'users.CustomUser'

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

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
