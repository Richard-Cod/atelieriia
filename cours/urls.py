from . import views
from django.urls import path



urlpatterns = [
    path('',views.all_cours,name='cours'),
    path('<str:nom>/<int:id>',views.do_cours,name='partie_cours'),

]