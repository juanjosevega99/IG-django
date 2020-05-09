"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.list_posts,
        name='feed'
    ),

    path(
        'posts/new/',
        view=views.create_post,
        name='create'
    ),
]
