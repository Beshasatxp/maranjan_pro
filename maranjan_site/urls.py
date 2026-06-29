from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # توجيه آمن لجميع روابط التطبيق
    path('community/', include('community.urls')),

]
