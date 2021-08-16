from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_hotel, name='add_hotels'),
    path('all', views.all_hotels, name='all_hotels'),
]