from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', login, {'template_name': 'login.html'}),
    url(r'^logout$', views.logout),
    url(r'^erro$', views.erro),
    ]