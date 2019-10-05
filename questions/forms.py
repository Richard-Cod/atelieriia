from django import forms
from django.contrib.auth.models import User

from .models import Question,Comment_to_question,Response_to_comments

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit , Layout,Field
from crispy_forms.bootstrap import PrependedText , PrependedAppendedText,FormActions

from django.db import models

class Questions_forms(forms.ModelForm):
	helper = FormHelper()
	helper.form_method = "POST"
	helper.add_input(Submit("Posez","Posez", css_class='btn-primary'))
	class Meta:
		model = Question
		fields = ('titre','body')


class CommentForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Comment_to_question
		fields=('text',)


class Response_to_comment_form(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Response_to_comments
		fields=('text',)