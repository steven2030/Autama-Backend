from django.urls import path
from . import views as AutamaProfile_views


app_name = 'AutamaProfiles'

urlpatterns = [
    path('', AutamaProfile_views.browse, name='browse'),
    path('register/', AutamaProfile_views.register_autama, name='register_autama'),
    path('robot/', AutamaProfile_views.RobotView.as_view(), name='robot'),
    path('<int:pk>-<slug:slug>/', AutamaProfile_views.profile, name='profile'),
]
