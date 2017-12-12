from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.relatorios),
    url(r'^semanal/', views.semanal),
    url(r'^mensal/', views.mensal),
    url(r'^anual/', views.anual),
    url(r'^contas/', views.conta),
    ]