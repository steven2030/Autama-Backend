from django.urls import path
from . import views as AutamaProfile_views


app_name = 'AutamaProfiles'

urlpatterns = [
    path('register/', AutamaProfile_views.register_autama, name='register_autama'),
    path('robot/', AutamaProfile_views.RobotView.as_view(), name='robot'),
    path('profile/', AutamaProfile_views.profile, name='profile'),
]
