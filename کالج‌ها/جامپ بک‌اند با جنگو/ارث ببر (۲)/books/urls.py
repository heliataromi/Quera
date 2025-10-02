from django.urls import path
from .views import book_list_view

urlpatterns = [
    path('', book_list_view, name='book_list'),
]
