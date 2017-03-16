from django.conf.urls import url
from . import views
from views import post_list
from views import post_detail


urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
] 
