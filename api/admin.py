from django.contrib import admin

from api.models import Student, Semester, Program, Lecturer, Enrollment

# Register your models here.
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Program)
admin.site.register(Lecturer)
admin.site.register(Enrollment)