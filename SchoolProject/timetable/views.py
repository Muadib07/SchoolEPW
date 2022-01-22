from django.shortcuts import render
from django.views.generic import ListView
import datetime

from .models import Lesson, Film
# from .filters import SchoolFilter
from .filters import FilmFilter


def test_view(request):
    lesson_list = Lesson.objects.all()
    #lesson_filter = SchoolFilter(request.GET, queryset=lesson_list)
    return render(request, "timetable_view/timetable/test.html", {'lesson_filter': lesson_list})

