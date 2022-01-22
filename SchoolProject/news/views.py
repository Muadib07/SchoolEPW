from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from taggit.models import Tag
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

from .models import SchoolNews
from .forms import SchoolNewsForm

def news_list(requst, tag_slug=None):
    news = SchoolNews.objects.all().order_by("-date_of_create")
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        news = news.filter(tags__in=[tag])

    paginator = Paginator(news, 3)
    page = requst.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(requst,
                  'news_view/news/list_news.html',
                  {'page': page,
                   'news': pages,
                   'tag': tag})


def news_detail(request, year, month, day, news):
    news = get_object_or_404(SchoolNews,
                             slug=news,
                             date_of_create__year=year,
                             date_of_create__month=month,
                             date_of_create__day=day)
    return render(request,
                  'news_view/news/detail_news.html',
                  {'news': news})


@staff_member_required
def delete_news(request, news_id):
    obj = get_object_or_404(SchoolNews, news_id=news_id)
    if request.method == "POST":
        obj.delete()
        return redirect("news_view:news_list")
    return render(request, 'news_view/news/delete_news.html')


def index(request):
    search_news = request.GET.get('search')
    if search_news:
        news = SchoolNews.objects.filter(Q(title__icontains=search_news) | Q(news_content__icontains=search_news))
    else:
        # If not searched, return default posts
        news = SchoolNews.objects.all().order_by("-date_of_create")
    return render(request, 'news_view/news/search_result.html', {'news': news})

@staff_member_required
def update_view(request, news_id):
    news = SchoolNews.objects.get(news_id=news_id)
    form = SchoolNewsForm(request.POST or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('news_view:list_news')
    return render(request, 'news_view/news/edit_news.html', {'news': news, 'form': form})