from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.main, name='main') #views.[something defined in views.py]
]
