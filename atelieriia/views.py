from django.shortcuts import render , get_object_or_404 ,redirect
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth import login

#from .models import Post,Comment
#from .forms import

from django.contrib.auth.decorators import login_required


def accueil(request):
	return render(request,'index.html',{})

def cours(request):
	return render(request,'cours.html',{})

def messages(request):
	return render(request,'messages.html',{})

def posts(request):
	return render(request,'posts.html',{})

def projets(request):
	return render(request,'projets.html',{})

def questions(request):
	return render(request,'questions.html',{})


def test(request):
	return render(request,'test.html',{})