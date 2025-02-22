from django.urls import path

from .views import login_view, Registerview, logout_user

urlpatterns = [
    path('login/',login_view, name='login'),
    path('register/',Registerview.as_view(), name='register' ),
    path('logout/', logout_user, name='logout')
]
 