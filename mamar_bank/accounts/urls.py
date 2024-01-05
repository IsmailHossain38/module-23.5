
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,UserBankAccountUpdateView,userlogout,pass_change
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', userlogout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('profile/pass_change', pass_change, name='pass_change' ),
]