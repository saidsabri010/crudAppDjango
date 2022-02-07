from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.


def index(request):
    search = request.POST.get('search')
    print(search)
    query = models.Post.objects.all().order_by('created_at')
    return render(request, 'index.html', {'data': query})


def showPost(request):
    form = forms.CreatePost()
    return render(request, 'showPost.html', {'form': form})


def searchPost(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        search_query = models.Post.objects.filter(title__icontains=search).all()
        return render(request, 'search.html', {'data': search_query})
    return redirect('index')


def addPost(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = forms.CreatePost()
    return render(request, 'showPost.html', {'form': form})


def showEditPost(request, id):
    query = models.Post.objects.filter(id=id)
    query1 = models.Category.objects.all()
    return render(request, 'ShowEditPost.html', {'post': query, 'categories': query1})


def editPost(request, id):
    if request.method == 'POST':
        query = models.Post.objects.get(id=id)
        query.title = request.POST.get("title")
        query.category_id = request.POST['category']
        query.body = request.POST.get("body")
        query.save()
        return redirect('index')
    return render(request, "ShowEditPost.html")


def deletePost(request, id):
    models.Post.objects.filter(id=id).delete()
    return redirect('index')
