from django.urls import path
from .views import main_view, home_view, list_view, edit_view, details_view, delete_post, like_list_view

urlpatterns = [
    path('',main_view,name='main'),
    path('home/', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('listing/<str:id>/edit/', edit_view, name='edit'),
    path('listing/<str:id>/details/', details_view, name='details'),
    path('listing/<str:id>/delete/', delete_post, name= 'delete'),
    path('listing/<str:id>/like/', like_list_view, name='like')
] 
