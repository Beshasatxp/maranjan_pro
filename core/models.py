from django.db import models

class SiteSetting(models.Model):
    key = models.CharField(max_length=100, unique=True, verbose_name="اسم الإعداد")
    value = models.TextField(verbose_name="القيمة أو المحتوى")
    description = models.CharField(max_length=200, blank=True, verbose_name="وصف")

    def __str__(self):
        return self.key

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="اسم الخدمة")
    link = models.CharField(max_length=200, verbose_name="الرابط")
    icon = models.CharField(max_length=50, verbose_name="الأيقونة (Emoji)")
    
    def __str__(self):
        return self.title
