from django.shortcuts import render
from .models import Blogpost

def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'index.html',
                  {'myposts': myposts})

def about(request):
    return render(request, 'about.html')
def categories(request):
    return render(request, 'categories.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blogpost.html',
                  {'post':post})
