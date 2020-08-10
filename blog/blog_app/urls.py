from django.contrib import admin
from django.urls import path,include
from blog_app import views
urlpatterns = [
    path("error/",views.error),
]
