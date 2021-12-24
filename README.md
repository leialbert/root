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

get the django path
```
python -c "import django; print(django.__path__)"
```
move the polls folder outside of the project folder,after that try to package it with setuptools.

after this , use this command to install it again. it works.
```
python -m pip install django-polls/dist/django-polls-0.1.tar.gz

# the original command is :
python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz

# but when you r using a virtualenv environment you will get an error.

ERROR: Can not perform a '--user' install. User site-packages are not visible in this virtualenv.
```

## I moved the folder from outside to project inside just because I want to upload to github and also copied back the polls app.

```
# because I want to check the source code , so I uninstall this package
python -m pip uninstall django-polls
```


