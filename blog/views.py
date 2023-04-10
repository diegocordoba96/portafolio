from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):

    post = Post.objects.all()

    return render(request, 'blog.html',{
        'post':post
    })

def blog_detalle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'blog_detalle.html',{
        'post': post
    })
  