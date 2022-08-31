"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&ko+k#xqjvo6@#5&i&i!it@wydy+%&)u#w3hst2m@l5+5&==-9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
    'gis.homtech.vn',
    'gis.homtech.vn:8000'
    'gis.homtech.vn:80'
]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'rest_framework_gis',
    'corsheaders',
    'eav',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/'),
        ],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#       'ENGINE': 'django.contrib.gis.db.backends.postgis',
#       'NAME': os.environ.get('POSTGRES_DB'),
#       'USER': os.environ.get('POSTGRES_USER'),
#       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#       'HOST': 'db',
#       'PORT': os.environ.get('PG_PORT'),
#    }
# }

DATABASES = {
    'default': {
      'ENGINE': 'django.contrib.gis.db.backends.postgis',
      'NAME': 'duanDB',
      'USER': 'postgres',
      'PASSWORD': 'admin',
      'HOST': 'localhost',
      'PORT': '5432',
   }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Saigon'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Media file
MEDIA_ROOT =  os.path.join(BASE_DIR, 'datastore')
MEDIA_URL = '/datastore/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Apps created
MY_APPS = [
    'nendialy',
    'biengioidiagioi',
    'cosododac',
    'dancu',
    'diahinh',
    'giaothong',
    'phubemat',
    'thuyvan',
    'soanthaokehoach',
    'myauth',
    'multimedia',
]

INSTALLED_APPS += MY_APPS

# 
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': '20',
    # 'DEFAULT_PARSER_CLASSES': [
        
    # ]
}


# Bật/tắt trang admin
ADMIN_ENABLED = True

# Bật tắt Swagger
SWAGGER_ENABLED = True
if SWAGGER_ENABLED:
    INSTALLED_APPS.append('drf_yasg')


# Tạo folder static cùng cấp manage.py
# Chạy câu lệnh python managr.py collectstatic
# STATIC_ROOT = 'static'


# 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# JAZZMIN SETTING
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Geo Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Geo",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Geo",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "books/img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Đăng nhập",

    # Copyright on the footer
    "copyright": "",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    # "topmenu_links": [

    #     # Url that gets reversed (Permissions can be added)
    #     {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

    #     # external url that opens in a new window (Permissions can be added)
    #     {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

    #     # model admin to link to (Permissions checked against model)
    #     {"model": "auth.User"},

    #     # App with dropdown menu to all its models pages (Permissions checked against models)
    #     {"app": "books"},
    # ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "soanthaokehoach"],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "soanthaokehoach": [{
    #         "name": "Make Messages", 
    #         "url": "make_messages", 
    #         "icon": "fas fa-comments",
    #         "permissions": ["soanthaokehoach.view_book"]
    #     }]
    # },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    # "language_chooser": True,
}


# SETTING BASE MAP GEOADMIN
# GEOADMIN_SETTINGS = {
#     "default_lon": float(os.environ.get('CENTER_LON')),
#     "default_lat": float(os.environ.get('CENTER_LAT')),
#     "default_zoom": int(os.environ.get('ZOOM')),
#     "display_wkt": False,
#     "display_srid": int(os.environ.get('CODE_CRS_DISPLAY')),
#     "extra_js": ['ol/js/proj4.js', 'ol/js/register_proj.js'],
#     "max_zoom": int(os.environ.get('MAX_ZOOM')),
#     "min_zoom": int(os.environ.get('MIN_ZOOM')),
#     "units": os.environ.get('UNIT_CRS_DISPLAY'),
#     "max_resolution": False,
#     "modifiable": True,
#     "mouse_position": True,
#     "scale_text": True,
#     "layerswitcher": True,
#     "scrollable": True,
#     "map_width": 600,
#     "map_height": 400,
#     "map_srid": int(os.environ.get('CODE_CRS_DB')),
#     "map_template": 'gis/admin/custom_geo_field/custom.html',
#     "openlayers_url": 'ol/js/ol.js',
#     "wms_url": os.environ.get('WMS_URL'),
#     "wms_layer": os.environ.get('WMS_LAYER'),
#     "wms_name": 'Viet Nam level 0',
#     "wms_options": {'format': os.environ.get('WMS_FORMAT'),}
# }

GEOADMIN_SETTINGS = {
    "default_lon": 105.5,
    "default_lat": 21,
    "default_zoom": 7,
    "display_wkt": False,
    "display_srid": 4756,
    "extra_js": ['ol/js/proj4.js', 'ol/js/register_proj.js'],
    "max_zoom": 18,
    "min_zoom": 4,
    "units": "degrees",
    "max_resolution": False,
    "modifiable": True,
    "mouse_position": True,
    "scale_text": True,
    "layerswitcher": True,
    "scrollable": True,
    "map_width": 600,
    "map_height": 400,
    "map_srid": 4756,
    "map_template": 'gis/admin/custom_geo_field/custom.html',
    "openlayers_url": 'ol/js/ol.js',
    "wms_url": "http://localhost:8080/geoserver/VietNam/wms",
    "wms_layer": "VietNam:VietNam_level_0",
    "wms_name": 'Viet Nam level 0',
    "wms_options": {'format': "image/png"}
}


# CORS
# CORS_ORIGIN_WHITELIST = [
#     'http://google.com',
#     'http://hostname.example.com',
#     'http://localhost:8000',
#     'http://127.0.0.1:9000'
# ]
CORS_ORIGIN_ALLOW_ALL=True
