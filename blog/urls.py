from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

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
	# Local url 
	# 127.0.0.1:8000/post/#/edit
	# Online url
	# mydjangosite.com/post/#/edit
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	# Local url 
	# 127.0.0.1:8000/drafts
	# Online url
	# mydjangosite.com/drafts
	path('drafts/', views.post_draft_list, name='post_draft_list'),
	# Local url 
	# 127.0.0.1:8000/post/2/publish
	# Online url
	# mydjangosite.com/post/2/publish
	path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
	# Local url 
	# 127.0.0.1:8000/accounts/login
	# Online url
	# mydjangosite.com/accounts/login
	# path('accounts/login/', auth_views.LoginView, name='login'),
	path('accounts/', include('django.contrib.auth.urls')),
]