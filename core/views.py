from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Service

from django.shortcuts import render
from .models import Service  # الموديل القديم لو موجود
from community.models import Post  # استيراد موديل المنشورات الجديد

def home(request):
    # جلب آخر 5 منشورات تم نشرها
    latest_posts = Post.objects.order_by('-created_at')[:5]
    
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'core/home.html', context) # تأكد من اسم ملف الـ html عندك

# 1. الصفحة الرئيسية
def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})

# 2. صفحة حجز الملاعب
def stadium_view(request):
    return render(request, 'stadium.html')

# 3. دالة مؤقتة لباقي الخدمات
def placeholder_view(request):
    return render(request, 'placeholder.html')

# 4. دالة التسجيل
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# 5. دالة تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 6. دالة تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect('core:index')
