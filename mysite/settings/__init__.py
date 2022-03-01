# settings/__init__.py

from .production import *

try:
    from .local_settings import *
except:
    pass
