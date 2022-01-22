import django_filters


from .models import Lesson


# class SchoolFilter(django_filters.FilterSet):
#     lesson_name = django_filters.CharFilter(lookup_expr='iexact')
#
#     class Meta:
#         model = Lesson
#         fields = ['lesson_name',]
#
