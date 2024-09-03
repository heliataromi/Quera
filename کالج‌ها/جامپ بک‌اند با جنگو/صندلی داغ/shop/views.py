from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)


def submit_person(request):
    if request.method == 'GET':
        form = PersonalInformation()
        return render(request, 'new_person.html', context={'form': form})

    elif request.method == 'POST':
        form = PersonalInformation(request.POST)
        if form.is_valid():
            person = Person()
            person.full_name = form.cleaned_data['full_name']
            person.gender = form.cleaned_data['gender']
            person.age = form.cleaned_data['age']
            person.height = form.cleaned_data['height']
            person.save()
            return HttpResponse(person, status=201)
