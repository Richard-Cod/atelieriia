from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('questions',views.questions,name="questions"),
    path('questions/<int:id>',views.questions_id,name="questions"),
    path('response_to_comment/<int:id>',views.response_to_comment,name="response_to_comment"),
]