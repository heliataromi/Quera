from django.urls import path

from watchlist.views import list_create_view

urlpatterns = [
    path('', list_create_view),
]