from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	titre = models.CharField(max_length=255,default='')
	body = models.TextField()
	date = models.DateTimeField(verbose_name="Date de parution",
                                default=timezone.now)

	def __str__(self):
		return self.user.username


class Comment_to_question(models.Model):
	question = models.ForeignKey('Question',on_delete=models.CASCADE,related_name='question')
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved = models.BooleanField(default=False)

	def approve(self):
		self.approved = True
		self.save()

	def __str__(self):
		return self.text


class Response_to_comments(models.Model):
	comment= models.ForeignKey('Comment_to_question',on_delete=models.CASCADE,related_name='reponses')
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved = models.BooleanField(default=False)

	def approve(self):
		self.approved = True
		self.save()

	def __str__(self):
		return self.text