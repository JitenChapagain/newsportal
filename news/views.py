from django.shortcuts import render, get_object_or_404
from .models import News

def index(request):
    sports_news = News.objects.filter(category__en_name='Sports', status=True)
    science_news = News.objects.filter(category__en_name='Science', status=True)
    astronomy_news = News.objects.filter(category__en_name='Astronomy', status=True)
    
    context = {
        'sports_news_with_index': [(index + 1, item) for index, item in enumerate(sports_news)],
        'science_news_with_index': [(index + 1, item) for index, item in enumerate(science_news)],
        'astronomy_news_with_index': [(index + 1, item) for index, item in enumerate(astronomy_news)],
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