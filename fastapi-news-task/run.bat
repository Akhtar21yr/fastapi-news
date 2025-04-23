@echo off
call venv\Scripts\activate

start cmd /k "fastapi dev app/main.py"
start cmd /k "celery -A app.celery_worker worker --pool=solo"
start cmd /k "celery -A app.celery_worker.celery_app beat --loglevel=info"

