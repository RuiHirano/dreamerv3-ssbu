build:
	docker build -t dreamerv3-ssbu:latest .
run:
	docker compose -f docker-compose.yml --env-file .env up -d
exec:
	docker exec -it dreamerv3-ssbu bash
remove:
	docker compose -f docker-compose.yml --env-file .env down
tensorboard:
	docker compose -f docker-compose.yml up -d tensorboard