from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework import status

class CustomAuthToken(ObtainAuthToken):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        if created:

            data = {
                'token': token.key,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'upload_url': 'http://127.0.0.1:8000/upload/clues/'}

            response = Response(data=data)
            return response

        return Response({"detail": "You have already got your token."}, status=status.HTTP_403_FORBIDDEN)
