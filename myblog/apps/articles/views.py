from django.shortcuts import render
from .models import Article, Category, Tag
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage


@login_required()
def index(request):
    # ?Все статьи которые не являются черновиком
    latest_articles_list = Article.objects.filter(is_draft=False).order_by('-pub_date')
    # ?Пагинация для статей
    p = Paginator(latest_articles_list, 3)
    page_num = request.GET.get('page', 1)
    total_pages = p.num_pages  # *Это нужно для того чтобы понять, отображать нам пагинацию или нет
    # !Проверяем, существует страница или нет. На случай если человек будет играться с адресной строкой браузера
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    # ?Популярные статьи для сайдбара
    popular_articles_list = Article.objects.filter(is_draft=False).order_by('views')[:5]
    # ?Категории для сайдбара
    latest_category_list = Category.objects.order_by('name')[:5]
    # ?Теги для сайдбара
    latest_tag_list = Tag.objects.order_by('name')[:10]

    context = {
        'total_pages': total_pages,
        'latest_articles_list': page,
        'latest_category_list': latest_category_list,
        'popular_articles_list': popular_articles_list,
        'latest_tag_list': latest_tag_list,
    }
    return render(request, 'articles/blog.html', context)


@login_required()
def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
        a.views = a.views + 1
        a.save()
    except:
        raise Http404("Статья не найдена!")

    latest_comment_list=a.comment_set.order_by('-id')[:10]
    popular_articles_list = Article.objects.filter(is_draft=False).order_by('views')[:5]
    latest_category_list = Category.objects.order_by('name')[:5]
    latest_tag_list = Tag.objects.order_by('name')[:10]

    context = {
        'article': a,
        'latest_comment_list': latest_comment_list,
        'latest_category_list': latest_category_list,
        'popular_articles_list': popular_articles_list,
        'latest_tag_list': latest_tag_list,
    }
    return render(request, 'articles/blog-single.html', context)


@login_required()
def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'], email=request.POST['email'], pub_date=datetime.now())

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


@login_required()
def categories(request):
    # ?Все категории
    all_categories = Category.objects.all()

    # ?Популярные статьи для сайдбара
    popular_articles_list = Article.objects.filter(is_draft=False).order_by('views')[:5]
    # ?Категории для сайдбара
    latest_category_list = Category.objects.order_by('name')[:5]
    # ?Теги для сайдбара
    latest_tag_list = Tag.objects.order_by('name')[:10]

    context = {
        'all_categories': all_categories,
        'latest_category_list': latest_category_list,
        'popular_articles_list': popular_articles_list,
        'latest_tag_list': latest_tag_list,
    }
    return render(request, 'articles/categories.html', context)


@login_required()
def tags(request):
    # ?Все теги
    all_tags = Tag.objects.all()

    # ?Популярные статьи для сайдбара
    popular_articles_list = Article.objects.filter(is_draft=False).order_by('views')[:5]
    # ?Категории для сайдбара
    latest_category_list = Category.objects.order_by('name')[:5]
    # ?Теги для сайдбара
    latest_tag_list = Tag.objects.order_by('name')[:10]

    context = {
        'all_tags': all_tags,
        'latest_category_list': latest_category_list,
        'popular_articles_list': popular_articles_list,
        'latest_tag_list': latest_tag_list,
    }
    return render(request, 'articles/tags.html', context)
