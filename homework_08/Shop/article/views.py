from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Group, Article
import json

# Create your views here.


def start_page(request):
    all_groups = Group.objects.all()

    context = {
        'all_groups': all_groups
    }

    return render(request, 'start_page.html', context=context)


class IndexListView(ListView):
    all_groups = Group.objects.all()
    model = Group
    context_object_name = 'group_all'
    template_name = 'start_page.html'


class ArticleDetailView(DetailView):
    model = Article
    #name = model #Article.objects.all()
    template_name = 'article_detail.html'
    #extra_context = {'name': name}