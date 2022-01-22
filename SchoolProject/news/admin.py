from django.contrib import admin
from .models import SchoolNews


@admin.register(SchoolNews)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'author', 'title', 'date_of_create', 'date_of_update',)
    list_filter = ('date_of_create', 'date_of_update',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    search_fields = ('title',)
    ordering = ('date_of_create',)