from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views

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
	# 127.0.0.1:8000/post/#/delete
	# Online url
	# mydjangosite.com/post/#/delete
	path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
	
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
	# 127.0.0.1:8000/post/2/comment
	# Online url
	# mydjangosite.com/post/2/comment
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	# Local url 
	# 127.0.0.1:8000/comment/2/remove
	# Online url
	# mydjangosite.com/comment/2/remove
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
	# Local url 
	# 127.0.0.1:8000/comment/2/approve
	# Online url
	# mydjangosite.com/comment/2/approve
	path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),

	# Local url 
	# 127.0.0.1:8000/signup
	# Online url
	# mydjangosite.com/signup
	path('signup/', views.signup, name='signup'),

]