from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm


class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
