from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsCharityOwner, IsBenefactor
from charities.models import Task, Benefactor
from charities.serializers import (
    TaskSerializer, CharitySerializer, BenefactorSerializer
)


class BenefactorRegistration(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        benefactor_serializer = BenefactorSerializer(data=request.data)
        if benefactor_serializer.is_valid():
            benefactor_serializer.save(user=request.user)
            message = benefactor_serializer.data
            return Response(message, status=status.HTTP_201_CREATED)

        return Response({'message': BenefactorSerializer.errors})


class CharityRegistration(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        charity_serializer = CharitySerializer(data=request.data)
        if charity_serializer.is_valid():
            charity_serializer.save(user=request.user)
            message = charity_serializer.data
            return Response(message, status=status.HTTP_201_CREATED)

        return Response({'message': CharitySerializer.errors})


class Tasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all_related_tasks_to_user(self.request.user)

    def post(self, request, *args, **kwargs):
        data = {
            **request.data,
            "charity_id": request.user.charity.id
        }
        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsCharityOwner, ]

        return [permission() for permission in self.permission_classes]

    def filter_queryset(self, queryset):
        filter_lookups = {}
        for name, value in Task.filtering_lookups:
            param = self.request.GET.get(value)
            if param:
                filter_lookups[name] = param
        exclude_lookups = {}
        for name, value in Task.excluding_lookups:
            param = self.request.GET.get(value)
            if param:
                exclude_lookups[name] = param

        return queryset.filter(**filter_lookups).exclude(**exclude_lookups)


class TaskRequest(APIView):
    permission_classes = (IsBenefactor,)

    def get(self, request, task_id):

        try:
            task = Task.objects.get(id=task_id)

        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if task.state != 'P':
            data = {'detail': 'This task is not pending.'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        task.state = 'W'
        task.assigned_benefactor = Benefactor.objects.get(user=request.user)
        task.save()
        data = {'detail': 'Request sent.'}
        return Response(data=data, status=status.HTTP_200_OK)


class TaskResponse(APIView):
    permission_classes = (IsCharityOwner,)

    def post(self, request, task_id, *args, **kwargs):
        if request.data['response'] not in ('A', 'R',):
            data = {'detail': 'Required field ("A" for accepted / "R" for rejected)'}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        task = Task.objects.get(id=task_id)
        if task.state != 'W':
            data = {'detail': 'This task is not waiting.'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        if request.data['response'] == 'A':
            task.state = 'A'
            task.save()

        if request.data['response'] == 'R':
            task.state = 'P'
            task.assigned_benefactor = None
            task.save()

        data = {'detail': 'Response sent.'}
        return Response(data=data, status=status.HTTP_200_OK)


class DoneTask(APIView):
    permission_classes = (IsCharityOwner,)

    def post(self, request, task_id, *args, **kwargs):
        try:
            task = Task.objects.get(id=task_id)

        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if task.state != 'A':
            data = {'detail': 'Task is not assigned yet.'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        task.state = 'D'
        task.save()
        data = {'detail': 'Task has been done successfully.'}
        return Response(data=data, status=status.HTTP_200_OK)
