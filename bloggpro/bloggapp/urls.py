from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import contact

urlpatterns = [
#    path('admin/', admin.site.urls),
    path('contact/',contact, name='contact'),
]
