from django.urls import path

from watchlist.views import list_create_view, detail_view, update_view, update_api_view

urlpatterns = [
    path('', list_create_view),
    path('<int:pk>/', detail_view),
    path('<int:pk>/edit/', update_view),
    path('api/update/<int:pk>/', update_api_view),
]