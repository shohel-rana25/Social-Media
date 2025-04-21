from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage_view, name='homepage'),
    path('create_post/', views.create_post_view, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]
