from django.urls import path

from . import views

app_name = 'timetable_view'

urlpatterns = [
    path('test/', views.test_view, name='search'),
]