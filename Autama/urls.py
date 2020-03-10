"""Autama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views as main_page_views  # from directory: Autama import view (the views.py file in this directory)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', auth_views.LoginView.as_view(), name='login'),
    path('', main_page_views.find_matches),
    # Include all auth views
    url('^', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls, name="admin"),
    path('about/', main_page_views.about, name="about"),
    path('homepage/', main_page_views.homepage, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('test_db_add/', main_page_views.test_db_add),
    path('test_db_lookup/', main_page_views.test_db_lookup),
    path('FindMatches/', main_page_views.find_matches, name="FindMatches"),
    path('MyMatches/', main_page_views.my_matches, name="MyMatches"),
    path('Chat/', main_page_views.chat, name="Chat"),
    path('logout/', main_page_views.pagelogout, name="logout")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
