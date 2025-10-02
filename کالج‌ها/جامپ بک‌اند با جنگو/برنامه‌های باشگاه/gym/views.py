from django.shortcuts import get_object_or_404, render, redirect

from gym.forms import CourseForm, EnrollmentForm
from gym.models import Course, Enrollment

def home(request):
    courses = Course.objects.all()
    return render(request, 'gym/home.html', {'courses': courses})


def enrollment_list(request, course_id=None):
    course = get_object_or_404(Course, pk=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    context = {'enrollments': enrollments, 'course': course}
    return render(request, 'gym/enrollment_list.html', context)


def create_course(request):
    if request.method == 'GET':
        form = CourseForm()
        return render(request, 'gym/create_course.html', {'form': form})

    elif request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request, 'gym/create_course.html', {'form': form})



def enroll(request, course_id):
    if request.method == 'GET':
        course = get_object_or_404(Course, pk=course_id)
        form = EnrollmentForm(course=course)
        return render(request, 'gym/enroll.html', {'form': form, 'course': course})

    elif request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        form = EnrollmentForm(course=course, data=request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()

            return redirect('home')

        return render(request, 'gym/enroll.html', {'form': form})