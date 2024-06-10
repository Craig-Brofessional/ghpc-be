# ghpc-be

heroku git:remote -a ghpc-be

# push and deploy
git push heroku main

heroku ps
heroku ps:scale web=0


# local
cd ~/Repos/ghpc-be
source .venv/bin/activate

pip install -r requirements.txt
heroku local --port 5001

# to exit
deactivate

# papertrail logs
heroku addons:open papertrail

# run a script in the context of your app, for example if you had cleanup/one-off scripts that need to be run:
https://devcenter.heroku.com/articles/getting-started-with-python#start-a-console


# interact with PostgreSQL
sudo su - postgres
psql


# Local setup:
sudo apt-get install postgresql
sudo apt-get install libpq-dev
sudo su postgres
psql
CREATE USER crode WITH PASSWORD '';
ALTER ROLE crode WITH SUPERUSER CREATEDB CREATEROLE REPLICATION BYPASSRLS;

https://stackoverflow.com/questions/69676009/psql-error-connection-to-server-on-socket-var-run-postgresql-s-pgsql-5432
sudo service postgresql restart

python manage.py makemigrations
python manage.py migrate


# Reset DB
// repeat for all created tables
DROP TABLE ghpc_pushup;
DROP TABLE ghpc_greeting;
TRUNCATE TABLE django_migrations;

python manage.py migrate --fake
python manage.py migrate ghpc 0001
