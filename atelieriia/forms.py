from django import forms
from django.contrib.auth.models import User

from .models import Profile,Question,Comment_to_question,Response_to_comments

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit , Layout,Field
from crispy_forms.bootstrap import PrependedText , PrependedAppendedText,FormActions

from django.db import models

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	helper = FormHelper()
	helper.form_method = "POST"
	helper.add_input(Submit("S'inscrire","S'inscrire", css_class='btn-primary'))

	class Meta:
		model = User
		fields = ('username','email','password')

	def clean(self):
	    cleaned_data = super(UserForm, self).clean()
	    username = cleaned_data.get('username')
	    email =  cleaned_data.get('email')
	    password =  cleaned_data.get('password')
	    if username:
	    	if username == 'probleme':
	    		raise forms.ValidationError("Pourquoi un nom d'utilisateur aussi bizarre ?")

	    if User.objects.filter(email=email).exists():
	    	raise forms.ValidationError("le mail existe deja")
	    elif email == "":
	    	raise forms.ValidationError("le champ mail ne peut être vide")

	    if User.objects.filter(username=username).exists():
	    	raise forms.ValidationError("le nom d'utilisateur est déja pris .Veuillez en essayer un autre")

	    mots_communs = ['123456','motdepasse','password']
	    if password:
	    	if password in mots_communs or len(password) <4:
	    		raise forms.ValidationError("Ce mot de passe est trop simple")

	    return cleaned_data

"""
class CViewerForm(forms.Form):
	class Meta:
		model = Profile
		fields = ('name','status','genre')"""

# accounts.models.py



class My_own_userForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('description','city','website','phone','avatar','genre')


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