from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vamar/', include('vamarapp.urls')),
    path('admin/', admin.site.urls),
]
