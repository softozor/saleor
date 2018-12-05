build:
	docker-compose build
init:
	docker-compose.exe run web python3 manage.py migrate
	docker-compose.exe run web python3 manage.py collectstatic
	docker-compose.exe run web python3 manage.py populatedb --createsuperuser


up:
	docker-compose.exe up