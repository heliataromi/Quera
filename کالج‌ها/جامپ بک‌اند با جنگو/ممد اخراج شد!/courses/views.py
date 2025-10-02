from django.shortcuts import render

from courses.models import Course

def detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/detail.html', {'course': course})

def list_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})
