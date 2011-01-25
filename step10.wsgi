# -*- coding: iso-8859-15 -*- 
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_prod'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
