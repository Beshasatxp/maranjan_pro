from django.shortcuts import render
from .models import Post

def news_list(request):
    # جلب كل المنشورات وترتيبها من الأحدث للأقدم
    posts = Post.objects.order_by('-created_at')
    return render(request, 'community/news.html', {'posts': posts})

