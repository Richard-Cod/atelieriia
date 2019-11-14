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
    #Vue de L'administration
    path('admin/', admin.site.urls),

    #Vue pour l'application atelieriia
    path('',views.accueil,name="accueil"),

    path('messages',views.messages,name="messages"),




    path('about',views.about,name="about"),

    
   
    #Toutes les vues de la partie registration
 	path('accounts/login/',auth_view.LoginView.as_view(),name='login'),
    path('accounts/logout/',auth_view.LogoutView.as_view(),name='logout',kwargs={'next_page': '/'}),
    path('signup',views.signup,name='signup'),

    #VUe de gestion de compte
    path('profile',views.profile,name="profile"),



    #Vue de l'application BLOG
     path('blog/',include('blog.urls')),
     

    #Vue de test
    path('test',views.test,name="test"),

    #Vue pour l'application de Question
    path('q/',include('questions.urls')),

    #Vue pour l'application de Cours
    path('cours/',include('cours.urls')),

    #Vue pour l'application de Projets
    path('projets/',include('projets.urls')),




     
     
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
