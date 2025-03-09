from django.urls import path
from .views import main_view, home_view, list_view, edit_view, details_view, delete_post, like_list_view, inquery_send_mail, users_profile_view

urlpatterns = [
    path('',main_view,name='main'),
    path('home/', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('listing/<str:id>/edit/', edit_view, name='edit'),
    path('listing/<str:id>/details/', details_view, name='details'),
    path('listing/<str:id>/delete/', delete_post, name= 'delete'),
    path('listing/<str:id>/like/', like_list_view, name='like_list'),
    path('listing/<str:id>/send_mail/', inquery_send_mail, name='send_mail'),
    path('listing/<str:id>/profile_view/', users_profile_view, name='profile_view')
    
] 
