clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run:clean
	elasticsearch
	python manage.py runserver --settings=search_hu.settings_local

migrations:clean
	python manage.py makemigrations --settings=search_hu.settings_local

migrate:clean
	python manage.py migrate --settings=search_hu.settings_local

shell:clean
	python manage.py shell --settings=search_hu.settings_local

tests:clean
	python manage.py test --settings=search_hu.settings_tests

install:
	sh install.sh
	pip install -r requirements.txt
	python manage.py makemigrations --settings=search_hu.settings_local
	python manage.py migrate --settings=search_hu.settings_local
	python manage.py bootstrap --settings=search_hu.settings_local
	python manage.py rebuild_index --settings=search_hu.settings_local

superuser:
	python manage.py createsuperuser --settings=search_hu.settings_local

rebuild_index:
	python manage.py rebuild_index --settings=search_hu.settings_local

locust:
	locust -f locustfile.py --host=http://localhost:8000
