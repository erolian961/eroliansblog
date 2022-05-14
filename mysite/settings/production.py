# settings/production.py

from .base import *
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

GOOGLE_ANALYTICS_TRACKING_ID='G-5BB3XX9FHP'

CLOUDINARY_STORAGE  = {
     'CLOUD_NAME':'hvpkxoza5',
     'API_KEY':os.environ.get('CLOUDDINARY_API_KEY'),
     'API_SECRET':os.environ.get('CLOUDDINARY_API_SECRET')
}
