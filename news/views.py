from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news = News.objects.all().filter(status=True)  # Filter only active news articles
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=True)  # Get the news article by slug
    return render(request, 'news_detail.html', {'news': news})
