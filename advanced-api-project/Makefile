.PHONY: allcommands

git:
	git add .
	git commit -m "Advanced API Development with Django REST Framework"
	git push

server:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

gitall:
	git add -A
	git commit -m "Advanced API Development with Django REST Framework"
	git push

superuser:
	python3 manage.py createsuperuser

