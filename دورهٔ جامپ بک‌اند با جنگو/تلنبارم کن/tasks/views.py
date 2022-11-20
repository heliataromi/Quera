from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        Task.objects.create(name=task_name)

        return HttpResponse(f"Task Created: '%s'" % task_name)
