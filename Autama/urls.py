"""Autama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
                       trying: from api.views import UserProfileViewSet
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
                       trying: path('', UserProfileViewSet.as_view(), name='user_profile')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
# from api.views import AllUserViewSet  # ?


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # path('', AllUserViewSet.as_view(), name='all_users'),  # ? nope
    # error msg: The `actions` argument must be provided when calling `.as_view()` on a ViewSet.
    # For example `.as_view({'get': 'list'})`
]


# OLD STUFF
# from django.contrib import admin
# from django.urls import path, include
# from . import views as main_page_views  # from directory: Autama import view (the views.py file in this directory)
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
# from django.conf import settings
# from django.conf.urls import url
# from django.contrib.auth import views as auth_views
#
#
# urlpatterns = [
#     #path('', auth_views.LoginView.as_view(), name='login'),
#     path('', main_page_views.FindMatches.as_view()),
#     # Include all auth views
#     url('^', include('django.contrib.auth.urls')),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('admin/', admin.site.urls, name="admin"),
#     path('about/', main_page_views.about, name="about"),
#     path('accounts/', include('accounts.urls')),
#     path('FindMatches/', main_page_views.FindMatches.as_view(), name="FindMatches"),
#     path('MyMatches/', main_page_views.MyMatches.as_view(), name="MyMatches"),
#     path('Chat/', main_page_views.chat_main_page, name="Chat_homepage"),
#     path('Chat/<int:pk>/', main_page_views.Chat.as_view(), name="Chat"),
#     path('logout/', main_page_views.LogoutView.as_view(), name="logout"),
#     path('AutamaProfiles/', include('AutamaProfiles.urls')),
# ]
#
# TODO: Is This Important?
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
