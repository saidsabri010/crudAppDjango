from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('showPost/', views.showPost, name='show'),
    path('addPost/', views.addPost, name='add'),
    path('showEdit/<id>', views.showEditPost, name='showEdit'),
    path('editPost/<id>', views.editPost, name='edit'),
    path('deletePost/<id>', views.deletePost, name='delete'),
    path('search/', views.searchPost, name='search')
]
