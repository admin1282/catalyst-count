<!-- /core
core/celery -A backend worker -l info -->



### Key Points Covered:

1. **Poetry Setup**: Installing dependencies with `poetry install`.
2. **Environment Variables**: Usage of `.env` file for database and Redis credentials.
3. **Database Migrations**: Run migrations with `poetry run python manage.py migrate`.
4. **Celery Setup**: Run Celery worker using `celery -A backend worker -l info`.
5. **Makefile Commands**: Use `make` to run common commands like `migrate`, `runserver`, and `celery`.
6. **Redis Setup**: Ensure Redis is installed and running.

