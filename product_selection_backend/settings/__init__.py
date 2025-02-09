import os

from .base import *

if os.environ.get("ENV_NAME") == 'Production':
    from .production import *
else:
    from .local import *
