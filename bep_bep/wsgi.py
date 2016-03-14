"""
WSGI config for bep_bep project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

try:
    # Add the site-packages of the chosen virtualenv to work with
    site.addsitedir(
        '/home/bepbep/.virtualenvs/bepbep/local/lib/python2.7/site-packages')

    # Add the app's directory to the PYTHONPATH
    sys.path.append('/home/bepbep/bep_bep')
    sys.path.append('/home/bepbep/bep_bep/bep_bep')

    from settings_production import *

    # Activate your virtual env
    activate_env = os.path.expanduser(
        "/home/bepbep/.virtualenvs/bepbep/bin/activate_this.py")
    execfile(activate_env, dict(__file__=activate_env))

except ImportError:
    pass

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bep_bep.settings")

application = get_wsgi_application()
