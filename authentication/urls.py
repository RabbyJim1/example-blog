from django.urls import path
from django.contrib import admin
from .views import SignUpView, LoginView

urlpatterns = [
    # path('login/', login),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
]
