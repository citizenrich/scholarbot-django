from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scholarbot.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(get_wsgi_application())
