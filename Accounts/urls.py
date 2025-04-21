from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_profile/', views.change_profile, name='change_profile'),
]
