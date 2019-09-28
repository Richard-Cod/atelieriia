from django.shortcuts import render , get_object_or_404 ,redirect
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import Profile
from .forms import UserForm,My_own_userForm


from django.contrib.auth.decorators import login_required





def accueil(request):
	membres =[
		{'nom':'Bathiebo',
		'prenom':'Richard',
		'description':'Je suis prési',
		},

		{'nom':'Meye',
		'prenom':'Yannick',
		'description':'Je suis responsable pedagogie'
		}
	]
	return render(request,'index.html',{'membres':membres})

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
	form = My_own_userForm
	return render(request,'test.html',{'form':form})


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

@login_required
def maj_info(request):
	profile = Profile.objects.filter(user=request.user) or None
	if request.method == 'POST':
		if Profile.objects.filter(user=request.user).exists():
			form = My_own_userForm(request.POST,request.FILES or None,instance=profile[0])
		else:
			form = My_own_userForm(request.POST,request.FILES or None)
	  
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('accueil')
	else:
		form = My_own_userForm()
	return render(request,'maj_info.html',{'form':form})

