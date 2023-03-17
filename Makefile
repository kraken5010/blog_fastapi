up:
	docker compose -f docker-compose.yml up -d

stop:
	docker compose -f docker-compose.yml down && docker network prune --force