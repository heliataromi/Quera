from django.urls import path
from .views import PostListCreateView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
