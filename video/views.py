from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator


# auth
def create(request):
    if request.method == 'GET':
        return render(request, 'video/create.html', context={'form': PostForm()})
    elif request.method == 'POST':
        field_form = PostForm(request.POST, request.FILES)
        field_form.save()
        return redirect('/video')


# auth
def delete(request, post_id):
    data = dict()
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        data['post'] = post
        return render(request, 'video/delete.html', context=data)
    elif request.method == 'POST':
        post.delete()
        return redirect('/video')


def details(request, post_id):
    data = dict()
    data['post'] = Post.objects.get(id=post_id)
    return render(request, 'video/details.html', context=data)


# auth
def edit(request, post_id):
    data = dict()
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        data['form'] = PostForm(instance=post)
        data['post'] = post
        return render(request, 'video/edit.html', context=data)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.about = form.cleaned_data['about']
            post.source = form.cleaned_data['source']
            post.image = form.cleaned_data['video']
            post.save()
        return redirect('/video')


def index(request):
    data = dict()
    all_posts = Post.objects.all()
    data['posts'] = all_posts
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'video/index.html', context=data)
