.PHONY: allcommands

git:
	git add .
	git commit "Advanced API Development with Django REST Framework"
	git push

server:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

gitall:
	git add -A
	git commit "Advanced API Development with Django REST Framework"
	git push

superuser:
	python manage.py createsuperuser

