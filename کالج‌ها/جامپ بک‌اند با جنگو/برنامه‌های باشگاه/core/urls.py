from django.urls import path, include

urlpatterns = [
    path('', include('gym.urls')),
]
