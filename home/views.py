from django.shortcuts import render
from video.models import Post
from django.core.paginator import Paginator


def index(request):
    data = dict()  # Словарь данных
    all_posts = Post.objects.all()
    data['posts'] = all_posts
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'home/index.html', context=data)


def about(request):
    return render(request, 'home/about.html')


def contacts(request):
    return render(request, 'home/contacts.html')
