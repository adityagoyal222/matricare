from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.http import HttpResponse

app_name="users"

def index(request):
    return HttpResponse("Hello logged in")

urlpatterns=[
    path('signup/',views.signUpView,name='signup_user'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('home/',index,name='index')
]