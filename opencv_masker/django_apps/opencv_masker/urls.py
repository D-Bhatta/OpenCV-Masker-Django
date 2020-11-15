from django.urls import path

from opencv_masker import views

app_name = "opencv_masker"

urlpatterns = [
    path("home/", views.homepage, name="homepage"),
    path("video/", views.video, name="video"),
    path("show_video/", views.show_video, name="show_video"),
    path("download/<str:filename>/", views.download, name="download"),
]
