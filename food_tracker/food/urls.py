from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . views import *


urlpatterns = [
    #url(r'^$',index,name='food-index'),
    url(r'^index/$',index,name='food-index'),
    url(r'^add_meals/$',add_meal,name='food-add-meal'),
    url(r'^update_meal/(?P<id>\d+)$',update_meal,name='food-update-meal'),
    url(r'^delete_meal/(?P<id>\d+)$',delete_meal,name='food-delete-meal'),
    url(r'^view_meal/(?P<id>\d+)$',view_meal,name='food-view-meal'),
    

	url(r'^$', login, name='login'),


]