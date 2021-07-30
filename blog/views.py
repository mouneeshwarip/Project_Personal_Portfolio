from django.shortcuts import render,get_object_or_404
from .models import blog_models

def all_blogs(request):
    blogs=blog_models.objects.order_by('date')
    return render(request,'blog/all_blogs.html',{'name':blogs})
def detail(request,blog_id):
    blog=get_object_or_404(blog_models,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})