from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def news_list(request):
    # جلب جميع المنشورات مع التعليقات الخاصة بها
    posts = Post.objects.prefetch_related('comments').all().order_by('-created_at')
    return render(request, 'community/news.html', {'posts': posts})

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        body = request.POST.get('body')
        if body:
            Comment.objects.create(post=post, user=request.user, body=body)
    return redirect('community:news_list')
