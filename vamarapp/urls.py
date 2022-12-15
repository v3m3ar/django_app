from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logout_page, name='logout'),
    path('message/', views.message_page, name='message'),
    path('friends/', views.friend_page, name='friends'),
    path('delete/', views.delete_page, name='delete'),
    path('', views.index, name='index'),
]
