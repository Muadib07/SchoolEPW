from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
from django.urls import reverse


class SchoolNews(models.Model):
    TARGET_GROUP = (
        ('A', 'All'),
        ('T', 'Teachers'),
        ('S', 'Students'),
    )
    news_id = models.BigAutoField(primary_key=True)
    target_group_news = models.CharField(max_length=1, choices=TARGET_GROUP)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='use_info',
                               verbose_name='Autor')

    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Tytuł')
    news_content = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Treść aktualności')

    date_of_create = models.DateTimeField(default=timezone.now, verbose_name='Data utworzenia')
    date_of_update = models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')

    slug = models.SlugField(max_length=100,
                            unique_for_date='date_of_create')

    tags = TaggableManager()

    class Meta:
        ordering = ('date_of_create',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_view:news_detail',
                       args=[self.date_of_create.year,
                             self.date_of_create.month,
                             self.date_of_create.day,
                             self.slug
                             ]
                       )

# news_image = models.ImageField(blank=True, null=True, upload_to='images/')
