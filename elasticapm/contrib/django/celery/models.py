"""
elasticapm.contrib.django.celery.models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2011-2017 Elasticsearch

Large portions are
:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if "djcelery" not in settings.INSTALLED_APPS:
    raise ImproperlyConfigured(
        "Put 'djcelery' in your INSTALLED_APPS setting in order to use the sentry celery client."
    )
