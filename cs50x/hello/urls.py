from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vraja", views.vraja, name="vraja"),
    path("<str:name>", views.greet, name="greet")
]