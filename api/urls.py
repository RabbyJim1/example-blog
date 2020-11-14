from django.conf.urls import url, include
from .views import GetPostsList, GetPostDetails, GetPostComments
from django.urls import path

# posts_urlpatterns = [
#     url(r"^posts/$", GetPostsList.as_view()),
#     url(r"^posts/(?P<post_id>\w+)/$", GetPostDetails.as_view()),
#     url(r"^posts/(?P<post_id>\w+)/comments/$", GetPostDetails.as_view()),
# ]


urlpatterns = [
    path('posts/', GetPostsList.as_view()),
    path('posts/<int:post_id>/', GetPostDetails.as_view()),
    path('posts/<int:post_id>/comments/', GetPostComments.as_view()),
]
