.PHONY: run-server
run-server:
	poetry run python core/manage.py runserver

.PHONY: migrations
migrations:
		poetry run python core/manage.py makemigrations

.PHONY: migrate
migrate:
		poetry run python core/manage.py migrate

.PHONY: shell
shell:
		poetry run python core/manage.py shell

.PHONY: superuser
superuser:
	poetry run python3.11 core/manage.py createsuperuser

.PHONY: update
update:
	poetry update

.PHONY: install
install:
	poetry install

.PHONY: flake8
flake8:
	poetry flake8 .

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run

.PHONY: test
test:
	poetry run pytest core