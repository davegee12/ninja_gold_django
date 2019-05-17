###Gold App###

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    # url('^process_money$', views.process_money),
    url('^farm$', views.farm),
    url('^cave$', views.cave),
    url('^house$', views.house),
    url('^casino$', views.casino),
    url('^reset$', views.reset),
]