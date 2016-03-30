clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run:clean
	python manage.py runserver --settings=geral.custom_settings

migrations:clean
	python manage.py makemigrations --settings=geral.custom_settings

migrate:clean
	python manage.py migrate --settings=geral.custom_settings

shell:clean
	python manage.py shell --settings=geral.custom_settings

tests:clean
	python manage.py test --settings=geral.settings_tests
