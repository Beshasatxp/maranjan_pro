from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
]
