import requests
from django.shortcuts import render


# POSTS VIEW ENDPOINT
def posts(request):
    return render(request, 'blog-listing.html')


def getPostListView(request):
    # 'https: // jsonplaceholder.typicode.com'
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    return render(request, 'blog-listing.html', {'response': response})


def getPostDetailView(request, post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}").json()
    comments = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments").json()
    return render(request, 'blog-post.html', {'response': response, 'comments': comments})


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')
