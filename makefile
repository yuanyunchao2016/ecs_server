test:
    python manager.py runserver

init:
    python manage.py makemigratons
    python manage.py migrate
    python manage.py createsuperuser



