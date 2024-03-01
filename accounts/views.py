from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LogoutView


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


