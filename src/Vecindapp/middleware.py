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
                if request.user.role == 1:
                    profile = request.user.r_profile
                    to_eval = (profile.building_num, profile.apartment_num, profile.parking_lot_num, profile.property_relation!=3)
                    if not all(to_eval):
                        if request.path not in [reverse('user:update_rprofile'), reverse('user:logout')]:
                            return redirect('user:update_rprofile')
                elif request.user.role == 2:
                    profile = request.user.w_profile
                    to_eval = (profile.id_num,)
                    if not all(to_eval):
                        if request.path not in [reverse('user:update_wprofile'), reverse('user:logout')]:
                            return redirect('user:update_wprofile')



        response = self.get_response(request)
        return response
