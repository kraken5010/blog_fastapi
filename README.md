Blog written in FastApi


RUN project

1. Install virtualenv

python3 -m venv env

2. Install requirements
 
pip install -r requirements.txt

3. Create .env file in /. 
For example:

DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
DB_HOST=localhost
DB_PORT=5432

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

3. Pull the database into docker

docker compose -f docker-compose.yml up -d

4. Do migrations
 
alembic upgrade head