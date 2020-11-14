from django.urls import path
from .views import SignUpView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
]
