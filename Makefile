mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

remove_migration:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

admin:
	python3 manage.py createsuperuser

celery:
	 celery -A root worker --loglevel=info
initdb:
	./init-db.sh
	python3 manage.py populate_user 20 populate_shop 5 populate_category 20 populate_product 40

freeze:
	pip freeze > requirements.txt
