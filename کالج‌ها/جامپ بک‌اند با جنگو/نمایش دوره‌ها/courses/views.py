from django.shortcuts import render

from courses.models import Course


def course_detail_view(request, course_id):
    course = Course.objects.get(id=course_id)

    context = {'course': course}
    return render(request, 'courses/course_detail.html', context)


def course_list_view(request):
    courses = Course.objects.all()
    ordering = request.GET.get('ordering', None)

    if ordering:
        if ordering == 'ASC':
            courses = courses.order_by('price')
        if ordering == 'DESC':
            courses = courses.order_by('-price')

    context = {'courses': courses,
               'ordering': ordering
               }
    return render(request, 'courses/course_list.html', context)