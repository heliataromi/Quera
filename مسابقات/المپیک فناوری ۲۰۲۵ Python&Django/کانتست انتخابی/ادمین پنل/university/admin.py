from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from university.models import *


class GPAFilter(SimpleListFilter):
    title = "GPA Range"

    parameter_name = "gpa"

    def lookups(self, request, model_admin):
        return (
            ('high', 'High (>= 85)'),
            ('medium', 'Medium (75–84)'),
            ('low', 'Low (< 75)'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'high':
            return queryset.filter(gpa__gte=85)
        if self.value() == 'medium':
            return queryset.filter(gpa__gte=75,
                                   gpa__lte=84)
        if self.value() == 'low':
            return queryset.filter(gpa__lte=75)
        return queryset


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    fields = ('course', 'semester', 'grade', 'grade_display')
    readonly_fields = ['grade_display']
    ordering = ['-semester']
    show_change_link = True
    can_delete = False

    def grade_display(self, obj):
        if obj.grade is not None:
            if obj.grade >= 85:
                return f"{obj.grade} (Excellent)"
            elif obj.grade >= 75:
                return f"{obj.grade} (Good)"
            else:
                return f"{obj.grade} (Needs Improvement)"
        return '-'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'enrollment_year', 'advisor', 'gpa_display', 'status_tag', 'course_count')
    list_display_links = ('full_name', 'email')

    sortable_by = ('full_name', 'enrollment_year', 'advisor')

    list_editable = ('enrollment_year',)

    list_filter = ('enrollment_year', 'is_active', 'advisor__department', GPAFilter)

    actions = ['deactivate_students', 'activate_students', 'delete_students']

    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email')
        }),
        ('Academic Information', {
            'fields': ('enrollment_year', 'advisor', 'is_active'),
        }),
        ('Statistics', {
            'fields': ('gpa_display', 'course_count'),
        }),
    )
    readonly_fields = ['gpa_display', 'course_count']

    inlines = [EnrollmentInline]

    def gpa_display(self, obj):
        gpa = obj.gpa()
        if gpa:
            return f'{obj.gpa():.2f}'
        return 'N/A'
    gpa_display.short_description = 'GPA'

    def status_tag(self, obj):
        return 'Active' if obj.is_active else 'Inactive'
    status_tag.short_description = 'Status'

    def course_count(self, obj):
        return obj.enrollment_set.count()
    course_count.short_description = 'Courses'

    def deactivate_students(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_students.short_description = "Deactivate selected students"

    def activate_students(self, request, queryset):
        queryset.update(is_active=True)
    activate_students.short_description = "Activate selected students"

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
