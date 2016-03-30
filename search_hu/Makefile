clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run:clean
	python manage.py runserver --settings=search_hu.settings_local

migrations:clean
	python manage.py makemigrations --settings=search_hu.settings_local

migrate:clean
	python manage.py migrate --settings=search_hu.settings_local

shell:clean
	python manage.py shell --settings=search_hu.settings_local

tests:clean
	python manage.py test --settings=search_hu.settings_tests
