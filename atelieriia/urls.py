"""atelieriia URL Configuration

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
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.accueil,name="accueil"),
    path('cours',views.cours,name="cours"),

    path('messages',views.messages,name="messages"),
    path('posts',views.posts,name="posts"),
    path('projets',views.projets,name="projets"),

    
    path('questions',views.questions,name="questions"),
    path('questions/<int:id>',views.questions_id,name="questions"),

 	path('accounts/login/',auth_view.LoginView.as_view(),name='login'),
    path('accounts/logout/',auth_view.LogoutView.as_view(),name='logout',kwargs={'next_page': '/'}),


     path('test',views.test,name="test"),
     path('signup',views.signup,name='signup'),

     path('blog/',include('blog.urls')),
     path('profile',views.maj_info,name="maj_info"),


     path('response_to_comment/<int:id>',views.response_to_comment,name="response_to_comment"),



     
     
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
