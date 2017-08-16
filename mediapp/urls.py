from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.photos, name='photos'),	
	url(r'^videos$', views.videos, name='videos'),	
	]
