# coding: utf-8
import logging

from settings import *


class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"



logging.disable(logging.INFO)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SOUTH_TESTS_MIGRATE = False
MIGRATION_MODULES = DisableMigrations()
SKIP_SLOW_TESTS = True
RUN_SLOW_TESTS = False
BROKER_BACKEND = 'memory'
CELERY_ALWAYS_EAGER = True
REUSE_DB=1
DATABASE_ROUTERS = []
