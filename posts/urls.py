from django.urls import path
from .views import posts, post_details, getPostListView, getPostDetailView

urlpatterns = [
    path('', getPostListView, name='home'),
    path('<int:post_id>/', getPostDetailView, name='post-details'),
]
