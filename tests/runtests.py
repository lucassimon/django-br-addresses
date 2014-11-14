#!/usr/bin/env python
import sys
import os
from django.core.management import execute_from_command_line
import django

if django.VERSION[:2] == (1, 7):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.conf import settings


def runtests():
    argv = [sys.argv[0], 'test']
    execute_from_command_line(argv)
    sys.exit(0)


if __name__ == '__main__':
    runtests()
