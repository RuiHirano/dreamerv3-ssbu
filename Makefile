build:
	docker build -t dreamerv3-ssbu:latest .
run:
	docker-compose -f docker-compose.yml up -d