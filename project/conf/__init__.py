from __future__ import absolute_import

from .base import *

try:
    if os.environ['ENV'] == 'prod':
        ENV = 'prod'
        from .prod import *
    else:
        ENV = 'dev'
        from .dev import *
except:
    ENV = 'dev'
    from .dev import *
