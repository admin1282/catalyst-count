# core/backend/__init__.py
from __future__ import absolute_import, unicode_literals

# Ensure that Celery is always imported when Django starts
from .celery import app as celery_app

__all__ = ('celery_app',)
