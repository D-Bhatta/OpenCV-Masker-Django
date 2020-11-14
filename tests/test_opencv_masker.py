""" Tests for 'project_name' package """
import pytest
from django.urls import reverse
from django_apps.utils import get_logger

lg = get_logger()

# This is supposed to fail
def test_helloworld():
    assert True == True


def test_view(client):
    url = reverse("opencv_masker:homepage")
    response = client.get(url)
    assert response.status_code == 200
