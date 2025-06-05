from django.urls import path

from .views import login_view, Registerview, logout_user, ProfileView, profile_redirect

urlpatterns = [
    path('login/',login_view, name='login'),
    path('register/',Registerview.as_view(), name='register' ),
    path('logout/', logout_user, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_redirect/',profile_redirect, name='profile_redirect')
    
]
 