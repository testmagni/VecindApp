# Django Imports
from django.urls import path

# Local Imports
from apps.users import views

urlpatterns = [
    path(
        route = 'signup/',
        view = views.SignUpView.as_view(),
        name = 'signup'
    ),
    path(
        route = 'login/',
        view = views.LoginView.as_view(),
        name = 'login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route = 'update/residente',
        view = views.ResidentProfileUpdateView.as_view(),
        name = 'update_rprofile'
    ),
    path(
        route = 'update/vigilante',
        view = views.WatchmanProfileUpdateView.as_view(),
        name = 'update_wprofile'
    ),
]
