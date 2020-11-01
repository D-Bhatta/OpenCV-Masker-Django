# OpenCV-Masker-Django

Notes and code about OpenCV-Masker-Django

## Sections

- [OpenCV-Masker-Django](#opencv-masker-django)
  - [Sections](#sections)
  - [Notes](#notes)
  - [Create project and deploy](#create-project-and-deploy)
    - [Main tasks](#main-tasks)
    - [Create a django project `django_apps`](#create-a-django-project-django_apps)
    - [Create a django app called `opencv_masker`](#create-a-django-app-called-opencv_masker)
    - [Deploy to pythonanywhere](#deploy-to-pythonanywhere)
  - [A homepage where people upload their videos through an upload form](#a-homepage-where-people-upload-their-videos-through-an-upload-form)
    - [Main tasks](#main-tasks-1)
    - [Create a view](#create-a-view)
    - [Create a homepage](#create-a-homepage)
    - [Add a form element with a dummy link](#add-a-form-element-with-a-dummy-link)
    - [Add the videos](#add-the-videos)
    - [Link the form](#link-the-form)
    - [Research how to upload files and use checklists](#research-how-to-upload-files-and-use-checklists)
  - [Additional Information](#additional-information)
    - [Screenshots](#screenshots)
    - [Links](#links)
  - [Notes template](#notes-template)

<!-- markdownlint-disable-file MD024 -->

## Notes

## Create project and deploy

- Create a django project
- Deploy to python anywhere

### Main tasks

- Create a django project `django_apps`
- Create a django app called `opencv_masker`
- Deploy to pythonanywhere

### Create a django project `django_apps`

- Create the project with `django-admin startproject django_apps`

### Create a django app called `opencv_masker`

- Create an app with `python manage.py startapp opencv_masker`
- Install app

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "opencv_masker",
]
```

- Run and refactor
- Remove secret key in `settings.py`

```python
SECRET_KEY = ""
```

- Add key generation utility in `utils.py` in `django_apps`

```python
from django.core.management.utils import get_random_secret_key


def generate_secret_key(env_file_name):
    r"""Generates a secret key and stores inside a `.env` file

    Generates a secret key for Django's `settings.py`. Stores it in a `.env`
    file with filename `env_file_name`.
    This can later be retrieved and set as an environment variable.

    Parameters
    ----------
    env_file_name : string
        Name of the `.env` file

    Returns
    -------
    None

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] Distributing Django projects with unique SECRET_KEYs
    https://stackoverflow.com/a/49362490

    Examples
    --------
    in the `setting.py` file of a django project, write the following lines of
    code. This will generate and set a DJANGO_SECRET_KEY as an environment
    variable.

    import dotenv
    from [project-folder-name] import utils
    ...
    try:
        SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    except KeyError:
        path_env = os.path.join(BASE_DIR, '.env')
        utils.generate_secret_key(path_env)
        dotenv.read_dotenv(path_env)
        SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    """
    with open(env_file_name, "a+") as f:
        generated_key = get_random_secret_key()
        f.write(f"DJANGO_SECRET_KEY = {generated_key}\n")
```

- Use `dotenv` to set environment variables in `settings.py`

```python
import dotenv
from django_apps import utils
import os

""" ... """

# Retrieve the environment variables

CONFIG_DIR = Path(__file__).resolve().parent.parent.parent.parent
try:
    path_env = os.path.join(CONFIG_DIR, ".env")
    dotenv.read_dotenv(path_env)
except EnvironmentError:
    print("Couldn't retrieve the environment variables")

try:
    path_env = os.path.join(CONFIG_DIR, ".env")
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
except KeyError:
    path_env = os.path.join(CONFIG_DIR, ".env")
    utils.generate_secret_key(path_env)
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
```

- Add to git
- Add static files in `django_apps/static/django_apps`
- Add a view to serve `dummy.html` at `masker/`

```python
"""django_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("opencv_masker/", include("opencv_masker.urls")),
]
```

```python
from django.urls import path

from opencv_masker import views

urlpatterns = [path("home/", views.homepage, name="homepage")]
```

```python
from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "dummy.html", {})
```

- Add `base.html` templates

```html
{% block header_content %} {% load static %}
<html>
  <meta charset="utf-8" />
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0, user-scalable=yes"
  />
  <link rel="stylesheet" href="{% static 'css/ridge.css' %}" />
  <link rel="stylesheet" href="{% static 'css/ridge-dark.css' %}" />
  {% endblock header_content %}
</html>

```

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["django_apps/templates/"],  # Add them here
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
```

- Add a `dummy.html` template

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<head>
  <title>Welcome to OpenCV Masker</title>
</head>
<body>
  <main>
    <vstack spacing="s" stretch="" align-x="center" align-y="center">
      <h1>This is a dummy test page</h1>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

- Run and refactor
- Modify settings to use 2 different values depending upon environment

```python
# Find out what environment we are running in
# Get the hostname
try:
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]
except KeyError:
    path_env = os.path.join(BASE_DIR, ".env")
    dotenv.read_dotenv(path_env)
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]

if DJANGO_ENVIRONMENT == "PRODUCTION":
    ALLOWED_HOSTS = [DJANGO_HOST_NAME]
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "django_apps/static/django_apps"),
        os.path.join(BASE_DIR, "opencv_masker/static/opencv_masker"),
    ]
elif DJANGO_ENVIRONMENT == "DEVELOPMENT":
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "django_apps\\static\\django_apps"),
        os.path.join(BASE_DIR, "opencv_masker\\static\\opencv_masker"),
    ]
    ALLOWED_HOSTS = []
else:
    pass

STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

- Run and refactor
- Add a logo

### Deploy to pythonanywhere

- Pull from git
- Create environment
- Install dependencies
- Collect static
- Follow tutorial [here](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- Working and source code directories are the ones with `manage.py` in them
- Add static assets
- Enable HTTPS
- Run and refactor

## A homepage where people upload their videos through an upload form

- Create a homepage with a heading and instructions and example videos
- Add a form with upload button and a check list with `blue` and `red` on it
- Link the form destination to it

### Main tasks

- Create a view
- Create a homepage
- Add a form element with a dummy link
- Add the videos
- Link the form
- Research how to upload files and use checklists

### Create a view

- Create a `homepage` view function
- Add an url to `home/`
- Serve `dummy.html`
- Run and refactor

### Create a homepage

- Create a `homepage.html`

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<head>
  <title>OpenCV Masker</title>
</head>
<body>
  <main>
    <vstack spacing="m">
      <vstack spacing="s" stretch="" align-x="center" align-y="center">
        <h1>Welcome to OpenCV Masker</h1>
        <p>Add instructions here</p>
      </vstack>
      <spacer></spacer>
      <vstack spacing="l">
        <vstack spacing="xs">
          <aside class="pa-s">
            <vstack>
              <form action="#" method="POST">
                <!-- {% csrf_token %} -->
                <vstack spacing="s">
                  <vstack>
                    <!-- {{form}} -->
                    <input type="file" name="video" id="video" />
                    <button type="upload" name="button">Upload Video</button>
                  </vstack>
                </vstack>
              </form>
            </vstack>
          </aside>
        </vstack>
      </vstack>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

- Add a heading
- Add a dummy instruction paragraph
- Add a form element
- Run and refactor

### Add a form element with a dummy link

- Create a `Form` in `forms.py` as `VideoUploadForm`
- Add a `TextField` with a `TextInput` `Widget`
- Add it to the `context` variable of the `homepage` view function
- Place it in `homepage.html`
- Run and refactor

### Add the videos

- Add an input and output video to `static/video` folder
- Add a `video` tag and serve the static videos
- Run and refactor

### Link the form

- Link the form to render `dummy.html`
- Link the form to the actual api view

### Research how to upload files and use checklists

- Research how to upload files and use checklists
- Create plan for it

## Additional Information

### Screenshots

### Links

## Notes template

```python
```

```html

```
