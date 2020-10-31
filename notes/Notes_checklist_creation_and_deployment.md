# Create project and deploy

- Create a django project
- Deploy to python anywhere

## Main tasks

- Create a django project `django_apps`
- Create a django app called `opencv_masker`
- Deploy to pythonanywhere

## Create a django project `django_apps`

- Create the project with `django-admin startproject django_apps`

## Create a django app called `opencv_masker`

- Create an app with `python manage.py startapp opencv_masker`
- Install app
- Run and refactor
- Remove secret key in `settings.py`
- Add key generation utility
- Use `dotenv` to set environment variables in `settings.py`
- Add to git
- Add static files
- Add a view to serve `dummy.html` at `masker/`
- Add `base.html` templates
- Add a `dummy.html` template
- Run and refactor
- Modify settings to use 2 different values depending upon environment
- Run and refactor

## Deploy to pythonanywhere

- Pull from git
- Create environment
- Collect static
- Follow tutorial [here](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- Add static assets
- Run and refactor
