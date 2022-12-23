# trading-app-api
Trading API project


docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose up

docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "python manage.py wait_for_db"
docker-compose run --rm app sh -c "python manage.py test && flake8"

docker-compose down

docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

docker volume ls

docker volume rm trading-app-api_dev-db-data

SUPERADMIN: superadmin@mail.com/superadmin

http://127.0.0.1:8000/api/docs/