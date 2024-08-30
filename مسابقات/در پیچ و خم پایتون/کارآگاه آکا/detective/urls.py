from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
]
