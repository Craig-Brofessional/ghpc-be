# ghpc-be

# push and deploy
git push heroku main

heroku ps
heroku ps:scale web=0


# windows
cd C:\Users\craig\Documents\Software\ghpc-be\
.\.venv\Scripts\activate

pip install -r requirements.txt
heroku local --port 5001 -f Procfile.windows


# linux
cd ~/Documents/repos/ghpc-be/
source .venv/bin/activate

pip install -r requirements.txt
heroku local --port 5001


# papertrail logs
heroku addons:open papertrail

# run a script in the context of your app, for example if you had cleanup/one-off scripts that need to be run:
https://devcenter.heroku.com/articles/getting-started-with-python#start-a-console