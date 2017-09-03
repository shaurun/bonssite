from django.shortcuts import render, get_object_or_404

# Create your views here.
from bonssite.models import Section, Article


def home(request):
    sections = Section.objects.all();
    context = {
        'sections': sections
    }
    return render(request, "bonssite/home.html", context);

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id);
    context = {
        'article' : article
    }
    return render(request, "bonssite/article.html", context);

