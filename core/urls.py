from django.contrib import admin
from django.urls import path


from app.views import homepage



urlpatterns = [
    path('', homepage, name= "home"),
    path('admin/', admin.site.urls),
]
