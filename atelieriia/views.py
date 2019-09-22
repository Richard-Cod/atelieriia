from django.shortcuts import render , get_object_or_404 ,redirect
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth import login

#from .models import Post,Comment
from .forms import UserForm


from django.contrib.auth.decorators import login_required





def accueil(request):
	if User.objects.filter(id=4).exists():
		print("T'inquiete ya pas de petard cest bien base")
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


def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request,new_user)
			return redirect('accueil')
	else:
		form = UserForm()
	return render(request,'registration/signup.html',{'form':form})
