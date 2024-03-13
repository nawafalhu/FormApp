from . import views
from django.urls import path

app_name = "lab5"
urlpatterns = [
    path("add/", views.index, name='index'),
    path("name/", views.main, name="main")
]