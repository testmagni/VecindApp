# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.
    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                if request.user.user_role == 1:
                    profile = request.user.r_profile
                    if not profile.picture or not profile.biography:
                        if request.path not in [reverse('users:update'), reverse('users:logout')]:
                            return redirect('users:update_rprofile')
                elif request.user.user_role == 2:
                    pass

        response = self.get_response(request)
        return response
