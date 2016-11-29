#!/usr/bin/env python
import os
import sys

try:
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
except:
    pass

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scholarbot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
