build:
	docker compose -f development/docker-compose.dev.yaml build --no-cache --build-arg UID=1000 --build-arg GID=1000
dev:
	docker compose -f development/docker-compose.dev.yaml run --entrypoint /bin/bash --service-ports --rm django
up:
	docker compose -f development/docker-compose.dev.yaml up
