from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المنشور")
    content = models.TextField(verbose_name="محتوى المنشور")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="الكاتب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")

    def __str__(self):
        return self.title

