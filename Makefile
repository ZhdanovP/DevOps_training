run:
	docker run -v ${PWD}:/usr/src/app --network host calculator python manage.py runserver
test:
	docker run -v ${PWD}:/usr/src/app --network host calculator py.test calculator/math_test.py
build:
	docker build -t calculator .
inspect:
	docker inspect calculator 