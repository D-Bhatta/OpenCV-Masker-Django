from os import remove
from shutil import copy, rmtree


def pytest_configure():
    copy(
        "opencv_masker/django_apps/django_apps/templates/base.html",
        "opencv_masker/django_apps/opencv_masker/templates",
    )


def pytest_unconfigure():
    remove("opencv_masker/django_apps/opencv_masker/templates/base.html")
