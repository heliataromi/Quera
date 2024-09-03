from .models import Profile


class ProfileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.profile = Profile.objects.get(user=request.user)

        response = self.get_response(request)
        return response
