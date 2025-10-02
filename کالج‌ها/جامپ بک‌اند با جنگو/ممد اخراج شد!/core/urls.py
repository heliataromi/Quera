from datetime import datetime

from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '', 
        TemplateView.as_view(template_name='home.html', extra_context={'year': datetime.now().year}),
        name='home'
    ),
    path(
        'about/', 
        TemplateView.as_view(template_name='about.html', extra_context={'year': datetime.now().year}),
        name='about'
    ),
    path(
        'courses/', 
        include('courses.urls', namespace='courses')
    ),
]
