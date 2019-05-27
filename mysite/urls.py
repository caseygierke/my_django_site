"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views	

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
   	# Local url 
	# 127.0.0.1:8000/accounts/login
	# Online url
	# mydjangosite.com/accounts/login
	# path('accounts/login/', auth_views.LoginView, name='login'),
	path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
	# path('accounts/', include('django.contrib.auth.urls')),
   	# Local url 
	# 127.0.0.1:8000/accounts/login
	# Online url
	# mydjangosite.com/accounts/login
	path('accounts/logout/', view=auth_views.LogoutView.as_view(), name='logout'),
	# path('accounts/', include('django.contrib.auth.urls'),name='logout', kwargs={'next_page': 'post_list'}),

]
