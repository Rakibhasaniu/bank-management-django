
from django.urls import path,include
from .views import UserRegisterView,UserLoginView,LogOutView

urlpatterns = [
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
