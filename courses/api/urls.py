from django.contrib import admin
from django.urls import path
from . import apiviews

app_name = 'api'
urlpatterns=[
    path('courselist/', apiviews.course_view, name = 'Course_list'),
]
