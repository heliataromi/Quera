from datetime import date
from django.shortcuts import render

from events.models import Event

def event_list_view(request):
    current_year = date.today().year
    events = Event.objects.filter(date__year=current_year).order_by('date')
    
    prepared_events = []
    for e in events:
        prepared_events.append({
            'title': e.title,
            'description': e.description,
            'date': e.date.strftime("%Y/%m/%d"),
            'month': e.date.strftime("%B"),
        })
    return render(request, 'events/event_list.html', {'events': prepared_events})
