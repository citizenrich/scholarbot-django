web: gunicorn scholarbot.wsgi
worker: celery -A scholarbot worker --loglevel info
beat: celery -A scholarbot beat --loglevel info
