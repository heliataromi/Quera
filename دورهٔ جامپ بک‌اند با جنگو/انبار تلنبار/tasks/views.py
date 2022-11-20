from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        if task_id in Task.objects.all().values_list('id', flat=True):
            task = Task.objects.get(id=task_id)
            task_name = task.name
            task.delete()

            return HttpResponse("Task Done: '%s'" % task_name)

        else:
            return HttpResponse("There isn't any task with id '%d'" % task_id)
