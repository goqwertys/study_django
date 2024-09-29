from tkinter.font import names

from django.urls import path
from skyblog.apps import SkyblogConfig

from skyblog.views import HomePostListView, BaseView, PostListView, CreatePostView, EditPostView, BlogPostDetailView, \
    OnModerationView, PostDeleteView

app_name = SkyblogConfig.name

urlpatterns = [
    # path('base', BaseView.as_view(), name='base'),
    path('', HomePostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('posts/new/', CreatePostView.as_view(), name='new_post'),
    path('posts/<int:pk>/edit/', EditPostView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('on_moderation/', OnModerationView.as_view(), name='on_moderation'),

]
