from django.urls import path, include
from . import views as AutamaProfile_views


app_name = 'AutamaProfiles'

urlpatterns = [
    path('', AutamaProfile_views.browse, name='browse'),

    path('register/', AutamaProfile_views.register_autama, name='register_autama'),
    path('<int:pk>-<slug:slug>/', AutamaProfile_views.profile, name='profile'),
    path('claim/', AutamaProfile_views.claim, name='claim'),
    path('inprogress/', AutamaProfile_views.autama_in_progress, name='autama_in_progress'),
]