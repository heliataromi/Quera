from django.urls import path

from gym import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_course, name='create_course'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('enrollments/', views.enrollment_list, name='all_enrollments'),
    path('enrollments/<int:course_id>/', views.enrollment_list, name='course_enrollments'),
]
