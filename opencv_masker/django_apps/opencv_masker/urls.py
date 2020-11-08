from django.urls import path

from opencv_masker import views

urlpatterns = [
    path("home/", views.homepage, name="homepage"),
    path("video/", views.video, name="video"),
]
