# Copyright (C) 2014-2015 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014-2015 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2015 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .development import *

#DEBUG = False

#ADMINS = (
#    ("Admin", "example@example.com"),
#)

DATABASES = {
    'default': {
        'ENGINE': 'transaction_hooks.backends.postgresql_psycopg2',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'thisisthetaigapassword',
        'HOST': 'postgres',
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "formatters": {
        "complete": {
            "format": "%(levelname)s:%(asctime)s:%(module)s %(message)s"
        },
        "simple": {
            "format": "%(levelname)s:%(asctime)s: %(message)s"
        },
        "null": {
            "format": "%(message)s",
        },
    },
    "handlers": {
        "null": {
            "level":"DEBUG",
            "class":"django.utils.log.NullHandler",
        },
        "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/taiga.log',
            'formatter': 'complete'
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django": {
            "handlers":["file"],
            "propagate": True,
            "level":"INFO",
        },
        "django.request": {
            "handlers": ["file", "mail_admins", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        "taiga": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": False,
        }
    }
}

#SITES = {
#    "api": {
#       "scheme": "http",
#       "domain": "localhost:8000",
#       "name": "api"
#    },
#    "front": {
#       "scheme": "http",
#       "domain": "localhost:9001",
#       "name": "front"
#    },
#}

#SITE_ID = "api"

MEDIA_URL = "http://" + os.getenv("API_NAME") + "/media/"
STATIC_URL = "http://" + os.getenv("API_NAME") + "/static/"

#PUBLIC_REGISTER_ENABLED = True

#MEDIA_ROOT = '/home/taiga/media'
#STATIC_ROOT = '/home/taiga/static'

# EMAIL SETTINGS EXAMPLE
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'
#DEFAULT_FROM_EMAIL = "john@doe.com"

# GMAIL SETTINGS EXAMPLE
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'taiga@gmail.com'
#EMAIL_HOST_PASSWORD = 'password'

# THROTTLING
#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec",
#    "import-dump-mode": "1/minute"
#}

# GITHUB SETTINGS
#GITHUB_URL = "https://github.com/"
#GITHUB_API_URL = "https://api.github.com/"
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"

# FEEDBACK MODULE (See config in taiga-front too)
#FEEDBACK_ENABLED = True
#FEEDBACK_EMAIL = "support@taiga.io"

# STATS MODULE
#STATS_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second

# SITEMAP
# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second
