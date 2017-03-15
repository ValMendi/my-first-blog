from django.conf.urls import include, url
from . import views
from views import post_list

urlpatterns = [
	url(r'^$', views.post_list),
] 
