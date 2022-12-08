from django.shortcuts import render
from .models import Blog

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/all_blog.html',{'blog':blog})