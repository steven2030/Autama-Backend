from django.urls import include, path
from api.routers import OptionalSlashRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# NOTE: URL patterns specify endpoints & where they go to

router = OptionalSlashRouter()
router.register(r'Users', views.UserViewSet)  # all users
router.register(r'Autamas', views.AutamaViewSet)  # all Autamas
router.register(r'Matches', views.MatchViewSet)  # all matches
router.register(r'Messages', views.MessageViewSet)  # all messages from all users and Autama
# ^^ can filter things using matchID?

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', obtain_auth_token, name='login')
]
