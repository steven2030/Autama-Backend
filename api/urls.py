"""api URL Configuration -- ? Copied from Autama/urls.py doc

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

from django.urls import include, path
from api.routers import OptionalSlashRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# NOTE: URL patterns specify endpoints & where they go to

router = OptionalSlashRouter()
router.register(r'User', views.UserViewSet)  # User info
router.register(r'Autama', views.AutamaViewSet)  # Autama info
router.register(r'Matches', views.MatchesViewSet)  # Matches
router.register(r'Messages', views.MessagesViewSet)  # Messages between user and Autama
# TODO: filter things using matchID, from the Matches model ^^


# added for testing
router.register('AllUsers', views.AllUsersViewSet)  # All User info
router.register('AllAutamas', views.AllAutamasViewSet)  # All Autama info


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='login'),  # 'login' or 'login/' ? also,  Webapp/login/
]
