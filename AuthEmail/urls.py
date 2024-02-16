from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin login
    path('admin/', admin.site.urls),
    # default path
    path ('', include('Main.urls')),
]
