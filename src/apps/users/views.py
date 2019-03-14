# Django Imports
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

# Local Imports
from .forms import SignUpForm


class SignUpView(FormView):
    """ Class based view for signup """
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:signin')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """ Class based view for login """
    template_name = 'users/signin.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'
