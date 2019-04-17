from django.urls import path
from . import views

urlpatterns = [
	# 127.0.0.1:8000 will take you to this.  
	path('', views.post_list, name='post_list'),
]