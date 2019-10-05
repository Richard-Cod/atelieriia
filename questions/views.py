from django.shortcuts import render , get_object_or_404 ,redirect,HttpResponseRedirect
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import Question,Comment_to_question,Response_to_comments
from .forms import Questions_forms,CommentForm,Response_to_comment_form


from django.contrib.auth.decorators import login_required




@login_required
def questions(request):
	if request.method == 'POST':
		form = Questions_forms(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('questions')
	else:
		form = Questions_forms()

	lesquestions = Question.objects.all().order_by('-date')
	return render(request,'questions.html',{'form':form,'questions':lesquestions})


@login_required
def questions_id(request,id):
	this = get_object_or_404(Question,id=id)


	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.question = this
			comment.user =request.user
			comment.save()
			return redirect('questions',id=id)
	else:
		form = CommentForm()

	response_to_comment_form=Response_to_comment_form()
	return render(request,'question_detail.html',{'this':this,'comment_form':form,'response_form':response_to_comment_form})



def response_to_comment(request,id):

	this = get_object_or_404(Comment_to_question,id=id)
	if request.method == 'POST':
		form = Response_to_comment_form(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.comment = this
			post.user =request.user
			post.save()

			next = request.POST.get('next','/')
			return HttpResponseRedirect(next)


	
	return redirect('accueil')