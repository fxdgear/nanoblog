import os
import sys
import site

PROJECT_ROOT = '/home/django/code/nanoblog/src/nanobog/nanoblog'
site_packages = '/home/django/code/nanoblog/lib/python2.7/site-packages'

site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(1, os.path.join(PROJECT_ROOT))
sys.path.insert(2, site_packages)
os.environ['DJANGO_SETTINGS_MODULE'] = 'nanoblog.settings'
os.environ['PYTHON_EGG_CACHE'] = '/home/django/.python-eggs'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()