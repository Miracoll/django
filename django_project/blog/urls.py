from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog-user/<int:pk>/', views.bloguser, name='blog-user'),
    path('post/<int:pk>/', views.postview, name='blog-post'),
    path('create-post/', views.CreateNewPost, name='create-post'),
    path('update-post/<int:pk>', views.updatepost, name='update-post'),
    path('delete-post/<int:pk>', views.deletepost, name='delete-post'),
    path('add-comment/', views.addcomment, name='comment'),
]
