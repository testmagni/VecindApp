# Django Imports
from django.urls import path

# Local Imports
from apps.home import views

urlpatterns = [
    path(
        route = '',
        view = views.index,
        name = 'welcome',
    )

]
