# flake8: noqa

import ast
import os

import dj_database_url

from .base import *


DEBUG = ast.literal_eval(os.environ.get('DEBUG', 'False'))
SECRET_KEY = os.environ.get('SECRET_KEY', None)

ALLOWED_HOSTS = ['.herokuapp.com', '0.0.0.0']


db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)


HAYSTACK_URL = os.environ.get('HAYSTACK_URL', None)
HAYSTACK_CONNECTIONS['default']['URL'] = HAYSTACK_URL
