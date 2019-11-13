from django.shortcuts import render , get_object_or_404 ,redirect,HttpResponseRedirect
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import Profile
from .forms import UserForm,My_own_userForm


from django.contrib.auth.decorators import login_required


from .mock_bureau import membres_bureau

from base64 import b64encode

with open("default-profile.png","rb") as f:
    z=f.read()
 


default_image_binary = b64encode(z).decode("utf-8")


def accueil(request):
	return render(request,'index.html',{})



def messages(request):
	return render(request,'messages.html',{})

def posts(request):
	return render(request,'posts.html',{})

def projets(request):
	return render(request,'projets.html',{})




def test(request):
	form = My_own_userForm
	return render(request,'test.html',{'form':form})


def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request,new_user)
			return redirect('profile')
	else:
		form = UserForm()
	return render(request,'registration/signup.html',{'form':form})

@login_required
def profile(request):
	profile = Profile.objects.filter(user=request.user) or None
	if request.method == 'POST':
		if Profile.objects.filter(user=request.user).exists():
			form = My_own_userForm(request.POST,request.FILES or None,instance=profile[0])
		else:
			form = My_own_userForm(request.POST,request.FILES or None)
	  
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			if 'avatar' in request.FILES:
				img_recu =request.FILES['avatar']
				image = b64encode(img_recu.read()).decode("utf-8")
				post.binaire= image

			if 'avatar-clear' in request.POST:
				post.binaire = default_image_binary
				print("zoumzoumlalamam")
			

			post.save()
			return redirect('accueil')

	else:
		if profile:
			form = My_own_userForm(instance=profile[0])
		else:
			form=My_own_userForm()
		

	return render(request,'registration/profile.html',{'form':form})





def bureau(request):
	return render(request,'bureau.html',{})

def about(request):
	return render(request,'about.html',{'membres_bureau':membres_bureau})