"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from wscubetech import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    
    path('about-us/', views.aboutUs),
    
    path('course/', views.course),
    path("course/<int:courseId>", views.courseDetails),
    
    path("teachers/", views.teachers),
    path("teachers/<str:teachersName>", views.teachersNames),
    
    path("students/", views.students),
    path("students/<slug:studentsDes>", views.studentsDescription),
    
    path("colleges/", views.colleges),
    path("colleges/<college_name>", views.collegesDetails),
    
    path('home/', views.homePage),
    path('data/', views.homeData),
    
    path('homeList/', views.homeList),
]
