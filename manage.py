#!/usr/bin/env python
import os
import os.path
import sys

from dotenv import Dotenv

if __name__ == "__main__":
    dotenv = Dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))
    os.environ.update(dotenv)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
