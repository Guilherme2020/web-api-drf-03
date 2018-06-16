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
    path("",views.ApiRoot.as_view()),
    path('admin/', admin.site.urls),
    path('users/',views.UserList.as_view(),name=views.UserList.name),
    path('users/<int:pk>/',views.UserDetail.as_view(),name=views.UserDetail.name),
    path('profiles/',views.ListProfileModel.as_view(),name=views.ListProfileModel.name),
    path('profiles/<int:pk>/',views.ListProfileModelDetail.as_view(),name=views.ListProfileModelDetail.name),

    path('comments/',views.ListPostCommentModel.as_view(),name=views.ListPostCommentModel.name),
    path('comments/<int:pk>',views.ListPostCommentModelDetail.as_view(),name=views.ListPostCommentModelDetail.name),

    path('profiles-post/',views.ListProfilePostsModel.as_view(),name=views.ListProfilePostsModel.name),
    path('profiles-post/<int:pk>/',views.ListProfilePostsModelDetail.as_view(),name=views.ListProfilePostsModelDetail.name),

    path('api-auth/', include('rest_framework.urls')),
]
