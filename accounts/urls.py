from django.urls import path
from . import views as accounts_views


app_name = 'accounts'  # For something akin to namespacing.

urlpatterns = [
    path('signup/', accounts_views.signup_view, name="signup"),
    path('profile/edit', accounts_views.edit_profile, name='edit_user_profile'),
    path('profile/', accounts_views.profile, name='view_user_profile')
]
