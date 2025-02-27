from django.urls import path
from .views import main_view, home_view, list_view, edit_view, details_view

urlpatterns = [
    path('',main_view,name='main'),
    path('home/', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('edit/', edit_view, name='edit'),
    path('details/', details_view, name='details')
]
