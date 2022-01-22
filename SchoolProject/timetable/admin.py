from django.contrib import admin
from .models import Student, Teacher, Subject, SchoolClass, Lesson, Film


@admin.register(Student)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('student_name',)


@admin.register(Subject)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('subject_name',)


@admin.register(Teacher)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'get_teachers_subject',)


@admin.register(SchoolClass)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'get_students', 'school_class_tutor',)


@admin.register(Lesson)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('lesson_day', 'lesson_teacher', 'lesson_subject',)





# @admin.register(Subject)
# class TaskAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(SchoolClass)
# class TaskAdmin(admin.ModelAdmin):
#     pass
