import os

env_name = os.getenv('ENV_NAME', 'prod')

if env_name == 'dev':
    from .dev import *
elif env_name == 'prod':
    from .prod import *
else:
    from .base import *