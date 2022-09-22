from django.conf import settings
from django.contrib import admin
from django.urls import path


from app.views import homepage



urlpatterns = [
    path('', homepage, name= "home"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)