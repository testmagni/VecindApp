# Django Imports
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Local Imports
from .forms import SignUpForm


class SignUpView(FormView):
    """ Class based vier for signup """
    template_name = 'users/signup.html'
    # form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
