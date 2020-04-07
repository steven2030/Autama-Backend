from django.urls import path
from . import views as accounts_views
from accounts.views import  *


app_name = 'accounts'  # For something akin to namespacing.

urlpatterns = [
    path('register/', accounts_views.RegisterView.as_view(), name="register"),
    #path('profile/edit', accounts_views.edit_profile, name='edit_user_profile'),
    path('profile/', accounts_views.ProfileView.as_view(), name='profile'),
    path('change-avatar/', ChangeAvatarView.as_view(), name='change-avatar'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
