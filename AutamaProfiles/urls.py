from django.urls import path, include
from . import views as AutamaProfiles_views


urlpatterns = [
    path('', AutamaProfiles_views.autama_profiles, name='autamaprofiles'),
    path('accounts/', include('accounts.urls'))
]