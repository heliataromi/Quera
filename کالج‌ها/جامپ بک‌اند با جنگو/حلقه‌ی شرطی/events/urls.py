from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list_view, name='event_list'),
]