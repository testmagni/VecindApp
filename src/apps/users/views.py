# Django Imports
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

# Local Imports
from .forms import SignUpForm, ResidentProfileUpdateForm, WatchmanProfileUpdateForm
from .models import ResidentProfile, WatchmanProfile


class SignUpView(FormView):
    """ Class based view for signup """
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """ Class based view for login """
    template_name = 'users/signin.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'


class ResidentProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Resident Profile View """
    template_name = 'users/profile_update.html'
    form_class = ResidentProfileUpdateForm
    model = ResidentProfile
    success_url = reverse_lazy('home:welcome')

    def get_object(self):
        """Return user's profile."""
        return self.request.user.r_profile


class WatchmanProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Resident Profile View """
    template_name = 'users/profile_update.html'
    form_class = WatchmanProfileUpdateForm
    model = WatchmanProfile
    success_url = reverse_lazy('home:welcome')

    def get_object(self):
        """Return user's profile."""
        return self.request.user.w_profile
