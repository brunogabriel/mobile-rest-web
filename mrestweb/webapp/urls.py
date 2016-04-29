from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
	url(r'^user/login$', views.do_login),
]
