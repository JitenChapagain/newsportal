from django.shortcuts import render, get_object_or_404
from .models import News

def index(request):
    news = News.objects.filter(status=True)  # Filter only active news articles
    news_with_index = [(index, item) for index, item in enumerate(news)]
    context = {
        'news_with_index': [(index + 1, item) for index, item in news_with_index]
    }
    return render(request, 'index.html', context)

def news_list(request):
    news = News.objects.all().filter(status=True)  # Filter only active news articles
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=True)  # Get the news article by slug
    return render(request, 'news_detail.html', {'news': news})

def about(request):
    return render(request,'aboutus.html')