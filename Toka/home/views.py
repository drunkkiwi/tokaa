from django.shortcuts       import render, HttpResponse
from .models                import NewsArticle
from datetime               import datetime, timedelta
from django.core.paginator  import EmptyPage, PageNotAnInteger, Paginator

# ============= HOME VIEW ===============
def home(request):

    NewsArticles = NewsArticle.objects.all().order_by('-id')

    paginator = Paginator(NewsArticles, 10)

    page = request.GET.get('page')
    paginated = paginator.get_page(page)

    context = {
        'Articles': paginated,
    }

    return render(request, 'home/home.html', context)



# ================ ARTICLE VIEW ====================
def article_view(request, title):

    cookieset = 'viewed_article' + title

    unique_article = NewsArticle.objects.get(article_slug=title)

    article_category = unique_article.article_category
    all_category_articles = NewsArticle.objects.filter(article_category=article_category).exclude(article_slug=title).order_by('-id')

    if cookieset in request.COOKIES:
        if request.COOKIES[cookieset] == 'yes':
            pass
        else:
            unique_article.article_views += 1;
            unique_article.save()
    else:
        unique_article.article_views += 1;
        unique_article.save()


    context = {
        'unique_article': unique_article,
        'all_category_articles': all_category_articles,
    }

    response = render(request, 'home/article_view.html', context)
    response.set_cookie(cookieset, 'yes')
    return response


# ====================== ABOUT VIEW ===================
def about(request):
    return render(request, 'home/about.html')



# ======================= CATEGORY VIEW =======================
def category_view(request, category):

    category_articles = NewsArticle.objects.filter(article_category=category).order_by('-id')
    try:
        category_full_name = NewsArticle.objects.filter(article_category=category)[0].get_article_category_display()
    except:
        category_full_name = "No articles"
    category_n = category

    paginator = Paginator(category_articles, 10)

    page = request.GET.get('page')
    paginated = paginator.get_page(page)

    context = {
        'Articles': paginated,
        'category': category_n,
        'category_name': category_full_name,
    }

    return render(request, 'home/category_view.html', context)


# =============== FLAKE VIEW ==============================
def flake_view(request):

    brendawhat = 'Më të shikuara brenda'

    raw_query = request.GET.get('d')
    if request.GET.get('d'):
        Articles = NewsArticle.objects.filter(article_created_at__gte=datetime.now()-timedelta(days=int(raw_query))).order_by('-article_views')
    else:
        Articles = NewsArticle.objects.filter(article_created_at__gte=datetime.now()-timedelta(days=7)).order_by('-article_views')

    if str(raw_query) == str(1):
        brendawhat = 'Brenda ditës'
    elif str(raw_query) == str(7):
        brendawhat = 'Brenda javës'
    elif str(raw_query) == str(31):
        brendawhat = 'Brenda muajit'
    else:
        pass


    paginator = Paginator(Articles, 10)

    page = request.GET.get('page')
    paginated = paginator.get_page(page)

    context = {
        'Articles': paginated,
        'raw_query': raw_query,
        'brendawhat': brendawhat,
    }

    return render(request, 'home/flake_view.html', context)