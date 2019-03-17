from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author':'Akash Dhar',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'22nd November, 2018' 
    },
    {
        'author':'Andrew Ng',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'1st December, 2018' 
    },
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request ,'blog/about.html',{'title':'about'})