import os
from confidence import Configuration
from confidence.presets import ProjectPreset, OptionsPreset, PostgreSQLPreset, RedisPreset

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

PROJECT_CONF = Configuration.compile_from_presets(os.path.join(PROJECT_ROOT, 'conf/project.conf'), [
    ProjectPreset(name='askme@sarafa2n', version='0.0.1', site_url='http://askme.sarafa2n.ru/'),
    OptionsPreset(secret_key=None, debug=None, allowed_hosts=['127.0.0.1']),
    PostgreSQLPreset(name=None, user=None, password=None, tcp_addr=None, tcp_port=5432),
])

PROJECT_NAME = PROJECT_CONF.get('project', 'name')

ALLOWED_HOSTS = PROJECT_CONF.get_csv('options', 'allowed_hosts')

PROJECT_VERSION = PROJECT_CONF.get('project', 'version')

DEBUG = PROJECT_CONF.get_bool('options', 'debug')

SECRET_KEY = PROJECT_CONF.get('options', 'secret_key') or 'secret'

SITE_URL = PROJECT_CONF.get('project', 'site_url')

PROJECT_APPS = [
    'core',
    'pages'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + PROJECT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'askme.urls'

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

WSGI_APPLICATION = 'askme.wsgi.application'


DATABASES = {}

DATABASE_SYSTEM = PROJECT_CONF.get('options', 'database')

if DATABASE_SYSTEM == 'postgresql':
    database_default_system_settings = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PROJECT_CONF.get('postgresql', 'name'),
        'USER': PROJECT_CONF.get('postgresql', 'user'),
        'PASSWORD': PROJECT_CONF.get('postgresql', 'password'),
        'HOST': PROJECT_CONF.get('postgresql', 'tcp_addr'),
        'PORT': PROJECT_CONF.get_int('postgresql', 'tcp_port'),
    }
else:
    database_default_system_settings = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

DATABASES['default'] = database_default_system_settings


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = ('%d %b %Y', '%d %b %Y')

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'uploads')

MEDIA_URL = '/uploads/'

FILE_UPLOAD_PERMISSIONS = 0o644
