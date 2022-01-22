from django.urls import path

from . import views

app_name = 'news_view'

urlpatterns = [
    path('list/', views.news_list, name='news_list'),
    path('tag/<slug:tag_slug>/', views.news_list, name='news_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:news>/', views.news_detail, name='news_detail'),
    path('<int:news_id>/delete/', views.delete_news, name='delete_news'),
    path('update/<news_id>', views.update_view, name='news_update'),
    path('', views.index, name="index"),

]

#path('detail/<int:id>', views.NewsDetailView.as_view(), name='news_detail'),
