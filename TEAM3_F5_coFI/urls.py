"""TEAM3_F5_coFI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path

from TEAM3_F5_coFI import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("userapp.urls")),
    path('', views.show_home, name='home'),
    path('communities/', include("articleapp.urls")),
    path('careers/', include("careerapp.urls")),
    path('mypage/', include("bookmarkapp.urls")),

    path('temp/', views.show_community, name='temp'),
    path('temp1/question/', views.show_article_list_question, name='temp1_question'),
    path('temp1/tip/', views.show_article_list_tip, name='temp1_tip'),
    path('temp1/free/', views.show_article_list_free, name='temp1_free'),
    path('temp2/', views.show_article_write, name='temp2'),


]
