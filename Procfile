web: gunicorn config.wsgi:application
worker: celery worker --app=djocker.taskapp --loglevel=info
