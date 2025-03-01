from django.urls import path
from .views import main_view, home_view, list_view, edit_view, details_view, delete_post

urlpatterns = [
    path('',main_view,name='main'),
    path('home/', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('edit/<str:id>/', edit_view, name='edit'),
    path('details/<str:id>/', details_view, name='details'),
    path('delete/<str:id>/', delete_post, name= 'delete')
] 
