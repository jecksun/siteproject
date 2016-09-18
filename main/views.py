from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from main.models import Article


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    return render(request, 'main/article.html', {'article':article})
