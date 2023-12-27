from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegisterForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.


class UserRegisterView(FormView):
    template_name='accounts/user_register.html'
    form_class= UserRegisterForm
    success_url=reverse_lazy('register')
    
    
    def form_valid(self, form):
        user= form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class LogOutView(LogoutView):
    def get_success_url(self) :
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    