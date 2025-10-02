from django.urls import path

from courses.views import course_list_view, course_detail_view

urlpatterns = [
    path('', course_list_view, name='course_list'),
    path('<int:course_id>/', course_detail_view, name='course_detail'),
]
