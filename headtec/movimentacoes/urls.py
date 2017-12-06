from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^saidas$', views.saidas),
    url(r'^entradas', views.entradas),
    url(r'^contas', views.contas),
    ]