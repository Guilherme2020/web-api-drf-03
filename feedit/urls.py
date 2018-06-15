"""feedit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from feeds import views

#from . import views
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
    path('profiles/',views.ListProfileModel.as_view(),name=views.ListProfileModel.name),
    path('profiles/<int:pk>/',views.ListProfileModelDetail.as_view(),name=views.ListProfileModelDetail.name),
    path('profiles-post/',views.ListProfilePostsModel.as_view(),name=views.ListProfilePostsModel.name),
    path('profiles-post/<int:pk>/',views.ListProfilePostsModelDetail.as_view(),name=views.ListProfilePostsModelDetail.name),
]
