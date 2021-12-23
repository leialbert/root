# learn django from the documentation

This is my learning project.

```
# env configure
virtualenv -p python3 env
pip install django
pip install django-debug-toolbar
mkdir root
mv env root
cd root
# create project
django-admin startproject mysite .
# create app
django-admin startapp polls
# migrate the defaut database
python manage.py migrate
# Create polls Models
python manage.py makemigrations polls

# check the SQL statement on your screen
python manage.py sqlmigrate polls 0001

# check running
python manage.py check

# running migrations
python manage.py check

# python shell
python manage.py shell

# create super user
python manage.py createsuperuser
```

Use gitignore file to ignore some files

```
git rm -r --cached some-directory
git commit -m 'Remove the now ignored directory "some-directory"'
git push origin master
```
