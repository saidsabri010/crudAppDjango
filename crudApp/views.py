from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models


# Create your views here.

def index(request):
    query = models.Post.objects.all()
    return render(request, 'index.html', {'data': query})


def showPost(request):
    form = forms.CreatePost()
    return render(request, 'showPost.html', {'form': form})


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
        # query1 = models.Category.objects.get(id=id)
        query.title = request.POST.get("title")
        query.category.name = request.POST.get("category")
        query.body = request.POST.get("body")
        query.save()
        return redirect('index')
    return render(request, "ShowEditPost.html")
