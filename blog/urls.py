from django.urls import path
from . import views

urlpatterns = [
	# Local url 
	# 127.0.0.1:8000 
	# Online url
	# mydjangosite.com
	path('', views.post_list, name='post_list'),
	# Local url 
	# 127.0.0.1:8000/post/2
	# Online url
	# mydjangosite.com/post/2
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	# Local url 
	# 127.0.0.1:8000/post/new
	# Online url
	# mydjangosite.com/post/new
	path('post/new/', views.post_new, name='post_new'),

]