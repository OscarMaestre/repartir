from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', inicio, name='inicio')
]
