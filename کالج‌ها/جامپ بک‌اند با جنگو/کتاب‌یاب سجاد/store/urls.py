from django.urls import path

from store.views import book_list

urlpatterns = [
    path('books/', book_list),
]