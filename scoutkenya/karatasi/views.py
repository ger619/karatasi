from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'karatasi/home.html', context)

def about(request):
    return render(request, 'karatasi/about.html', {'title' :'About'} )
#
