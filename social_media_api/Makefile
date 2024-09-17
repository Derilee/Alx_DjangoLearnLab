.PHONY: allcommands

git:
	git add .
	git commit -m 'Building and deploying a Django API'
	git push

migrate:
	python manage.py makemigrations
	python manage.py migrate

server:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver