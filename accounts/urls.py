
from django.urls import path,include
from .views import UserRegisterView,UserLoginView,LogoutViewS,UserBankAccountUpdateView

urlpatterns = [
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutViewS.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
]
