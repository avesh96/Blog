"""bloggpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from bloggapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bloggapp/', include('bloggapp.urls')),
    path('',home,name = "home"),
    path('about/',about,name = "about"),
    #path('contact/',contact,name = "contact"),
    #path('success/',success,name = "success"),
    path('user_signup/',user_signup,name = "signup"),
    path('user_login/',user_login,name="login"),
    path('dashboard/',dashboard,name="dashboard"),
    path('user_logout/',user_logout,name="logout"),
    path('addpost/',addpost,name="addpost"),
    path('updatepost/<int:id>/',updatepost,name='updatepost'),
    path('deletepost/<int:id>/',deletepost,name="deletepost"),
    path('delc',deleting_cookie, name='delc'),
    #path('dashboard/',Dashboard.as_view(),name='dashboard'),
    #path('addpost',AddPost.as_view(),name='addpost')
    #path( "*/migrations/*.py", not name= "__init__.py" -delete)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
