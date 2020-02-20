from django.urls import path
from . import views


app_name = 'accounts'  # For something akin to namespacing.

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
]
