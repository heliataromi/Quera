from django.urls import path

from .views import login, Logout, Register

urlpatterns = [
    path('login/', login),
    path('logout/', Logout.as_view()),
    path('register/', Register.as_view())
]
