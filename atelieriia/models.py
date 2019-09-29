
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
"""
class Profile(models.Model):
    name = models.CharField(max_length=100)    
    status = models.IntegerField(choices=((1, ("Not relevant")),
									    (2, ("Review")),
									    (3, ("Maybe relevant")),
									    (4, ("Relevant")),
									    (5, ("Leading candidate"))), default=1) 
"""

class Profile(models.Model):
	user= models.OneToOneField(User,on_delete=models.CASCADE)
	description = models.CharField(max_length=100,default='')
	city = models.CharField(max_length=100,default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	avatar = models.ImageField(upload_to='avatars/',blank=True,default='avatars/no.png')
	genre = models.IntegerField(choices=((1, ("Homme")),
									    (2, ("Femme")))
								)

	def __str__(self):
		return self.user.username
	

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