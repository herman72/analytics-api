# analytics-api


## Docker
- `docker build -t analytics-app -f Dockerfile.web .`
- `docker run analytics-app`

becomes

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v` (to remove volumes)
- `docker compose run app /bin/bash` or `docker compose run app python` 