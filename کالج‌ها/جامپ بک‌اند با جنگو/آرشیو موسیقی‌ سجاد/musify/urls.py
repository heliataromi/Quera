from django.urls import path

from musify.views import list_create_view, retrieve_update_delete_view

urlpatterns = [
    path("", list_create_view, name="list-create"),
    path("<int:pk>/", retrieve_update_delete_view, name="retrieve-update-delete"),
]
