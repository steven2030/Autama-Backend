from django.urls import include, path
from api.routers import OptionalSlashRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = OptionalSlashRouter()
router.register(r'users', views.UserViewSet)
router.register(r'ais', views.AIViewSet)
router.register(r'messages', views.MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', obtain_auth_token, name='login')
]
