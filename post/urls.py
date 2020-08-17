from django.urls import path, include
from .views import helloAPI, totalPost

urlpatterns = [
    path("hello/", helloAPI),
    path("post/", totalPost),
]