from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import json
from django.http import JsonResponse
from django.db.models import F


def home(request):

    projects = Project.objects.order_by('-id')
    categories = Category.objects.all()
    tags_popular = Tag.objects.order_by('-views')[:8]

    context = {
        'title': 'Главная',
        'projects': projects,
        'categories': categories,
        'tags_popular': tags_popular,
    }

    return render(request, 'home.html', context)


def project_detail(request, project_detail_slug):

    project = Project.objects.get(slug=project_detail_slug)

    context = {
        'title': project.name,
        'project': project,
    }

    return render(request, 'project_detail.html', context)


def search(request):

    search_value = request.GET.get('search')
    if search_value:
        projects = Project.objects.filter(name__icontains=search_value)
    else:
        projects = Project.objects.all()

    context = {
        'projects': projects,
        'search_value': search_value,
    }

    return render(request, 'search.html', context)


def filter_fetch(request):

    categories_fetch = json.loads(request.body.decode())
    categories = []
    for cat in categories_fetch:
        if categories_fetch[cat]['checked']:
            category = Category.objects.get(id=cat)
            categories.append(category)

    if not categories:
        categories = Category.objects.all()

    projects = []
    for cat in categories:
        for proj in cat.project_set.all():
            words = proj.description.split()
            first_20_words = words[:20]
            description = ' '.join(first_20_words)

            proj_obj = {
                'url': proj.get_absolute_url(),
                'photo': proj.photo.url,
                'name': proj.name,
                'description': description,
                'name_team': proj.name_team,
            }
            projects.append(proj_obj)

    obj = {
        'status': 'ok',
        'projects': projects,
    }

    return JsonResponse(obj)


def tag_detail(request, tag_detail_slug):

    tag = get_object_or_404(Tag, slug=tag_detail_slug)
    tag.views = F('views') + 1
    tag.save()
    tag.refresh_from_db()  # Вся эта процедура выясняет самую популярную категорию. При переходе увеличивается поле views на 1
    projects = Project.objects.filter(tag__id=tag.id)

    context = {
        'title': f'Проекты по тегу {tag.name}',
        'tag': tag,
        'projects': projects,
    }

    return render(request, 'category_detail.html', context)
