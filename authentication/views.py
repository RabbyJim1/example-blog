from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin


# LOGIN VIEW ENDPOINT

# def login(request):
#     return render(request, 'login.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class LoginView(auth_views.LoginView, SuccessMessageMixin):
    form_class = CustomUserAuthenticationForm
    template_name = 'login.html'
