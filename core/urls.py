from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # المسارات الرئيسية
    path('', views.index, name='index'),
    path('stadium/', views.stadium_view, name='stadium'),

    # مسارات الخدمات
    path('emergency/', views.placeholder_view, name='emergency'),
    path('utilities/', views.placeholder_view, name='utilities'),
    path('market/', views.placeholder_view, name='market'),
    path('news/', views.placeholder_view, name='news'),
    path('cleaning/', views.placeholder_view, name='cleaning'),
    path('charity/', views.placeholder_view, name='charity'),
    path('pharmacy/', views.placeholder_view, name='pharmacy'),

    # مسارات الحسابات (هنا التعديل المهم)

# تأكد أن هذه الأسطر مكتوبة بهذا الشكل بالضبط في ملف core/urls.py
path('register/', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
]
