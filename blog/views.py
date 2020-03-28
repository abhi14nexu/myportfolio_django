from django.shortcuts import render, get_object_or_404
from .models import blogs

# Create your views here.
def allblogs(request):
    blog = blogs.objects
    return render(request, 'blog/allblogs.html', {'blog':blog})
  # return render(request,'jobs/home.html',{'jobs':jobs})

def detail(request,blog_id):
 detailblog=get_object_or_404(blogs,pk=blog_id)
 return render(request,'blog/detail.html',{'blog':detailblog})

