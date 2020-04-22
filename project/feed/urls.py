from django.urls import path

from .views import *


app_name = 'feed'


urlpatterns = [
    path('create-post',CreatePostView,name='create-post'),
    path('list-posts',ListPostsView.as_view(),name='list-posts'),
    path('tag/<slug:slug>/', tagged, name="tagged"),
]