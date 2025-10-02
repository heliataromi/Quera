from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('courses/', include('courses.urls')),
    path('about/', TemplateView.as_view(template_name='about.html')),
]
