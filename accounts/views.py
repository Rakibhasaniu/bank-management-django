from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegisterForm
from django.contrib.auth import login,logout
# Create your views here.


class UserRegisterView(FormView):
    template_name=''
    form_class= UserRegisterForm
    success_url=''
    
    
    def form_valid(self, form):
        user= form.save()
        login(user)
        return super().form_valid(form)
    
    