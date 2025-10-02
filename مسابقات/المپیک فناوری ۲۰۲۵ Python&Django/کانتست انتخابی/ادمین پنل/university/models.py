from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    head_of_department = models.ForeignKey(
        'Professor', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='headed_departments'
    )

    def __str__(self):
        return f"{self.name} ({self.code})"


class Professor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_year = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    advisor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def gpa(self):
        grades = self.enrollment_set.exclude(grade__isnull=True).values_list('grade', flat=True)
        if grades:
            return round(sum(grades) / len(grades), 2)
        return None


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.PositiveSmallIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(Professor)

    def __str__(self):
        return f"{self.title} ({self.code})"

    def student_count(self):
        return self.enrollment_set.count()


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    grade = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course', 'semester')

    def __str__(self):
        return f"{self.student} - {self.course} ({self.semester})"
