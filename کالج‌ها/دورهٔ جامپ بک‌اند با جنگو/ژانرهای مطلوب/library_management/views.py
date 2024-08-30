from django.http import JsonResponse


def books(request, genre) -> JsonResponse:
    """get list of IDs of books based on genre"""
