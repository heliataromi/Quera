from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .serializers import UserSerializer

login = obtain_auth_token


class Logout(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"Bye {request.user.username}!"}, status=status.HTTP_204_NO_CONTENT)


class Register(CreateAPIView):
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            message = user_serializer.data
            return Response(message, status=status.HTTP_201_CREATED)

        return Response({'message': UserSerializer.errors})
