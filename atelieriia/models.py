from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
	

