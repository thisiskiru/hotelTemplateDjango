from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about-us',views.about_us,name='about-us'),
    path('rooms',views.rooms,name='rooms'),
    path('whattosee',views.whattosee,name='whattosee'),
    path('contact',views.contact,name='contact'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name = 'logout'),
    path('dashboard',views.dashboard,name = 'dashboard'),
    path('change_password', views.change_password, name='change_password'),
    
]