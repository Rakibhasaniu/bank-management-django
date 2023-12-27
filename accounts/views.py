from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegisterForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy

# Create your views here.


class UserRegisterView(FormView):
    template_name='accounts/user_register.html'
    form_class= UserRegisterForm
    success_url=reverse_lazy('register')
    
    
    def form_valid(self, form):
        user= form.save()
        login(user)
        return super().form_valid(form)
    
    