# Django Imports
from django.urls import path

# Local Imports
from apps.users import views

urlpatterns = [
    path(
        route = 'signup/',
        view = views.SignUpView.as_view(),
        name = 'signup'
    )
]
