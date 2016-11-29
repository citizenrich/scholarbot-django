web: gunicorn scholarbot.wsgi
worker: celery -A scholarbot worker -l info
beat: celery -A scholarbot beat -l info
