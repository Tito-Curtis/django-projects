from django.urls import path,re_path # p [
from app import views

urlpatterns = [
    
    path('meetings/<int:id>', views.details, name='meetings'),
    path('room/', views.all_room, name='room'),
    path('new/', views.new, name='new'),
    path('signup/', views.signUp_view, name='signup'),
    
    
]