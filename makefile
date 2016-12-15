test:
	python manage.py runserver

init:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser



