build:
	docker build -t bugs .
up:
	docker run -it -p 5000:5000 bugs flask run --host=0.0.0.0