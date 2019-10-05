from django.shortcuts import render , get_object_or_404 ,redirect,HttpResponseRedirect
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





"""
@login_required
def questions_id(request,id):
	this = get_object_or_404(Question,id=id)

	if request.method == 'POST':
		if 'commentaire' in request.POST:
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.question = this
				comment.user =request.user
				comment.save()
				return redirect('questions',id=id)

		elif 'reponse_to_comment' in request.POST:
			response_to_comment_form = Response_to_comment_form(request.POST)
			if form.is_valid():
				post = response_to_comment_form.save(commit=False)
				post.comment = this
				post.user =request.user
				post.save()
				return redirect('questions',id=id)

	else:
		form = CommentForm()
		response_to_comment_form=Response_to_comment_form()

	return render(request,'question_detail.html',{'this':this,
												  'comment_form':form,
												  'response_form':response_to_comment_form})

"""