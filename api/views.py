import requests
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class GetPostsList(APIView):
    def get(self, request, format=None):
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        return Response(r.json())


class GetPostDetails(APIView):
    def get(self, request, post_id, format=None):
        r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        return Response(r.json())


class GetPostComments(APIView):
    def get(self, request, post_id, format=None):
        r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
        return Response(r.json())
