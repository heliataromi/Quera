from django.http import HttpResponse

from .models import Task


def list_create_tasks(request):
    if request.method == 'GET':
        response = Task.objects.all().order_by('name').values_list('name', flat=True)
        return HttpResponse('<br>'.join(response))


def count_tasks(request):
    if request.method == 'GET':
        response = Task.objects.all().count()
        return HttpResponse(f"You have '%d' tasks to do" % response)
