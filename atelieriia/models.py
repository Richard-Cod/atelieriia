from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from base64 import b64encode

with open("default-profile.png","rb") as f:
    z=f.read()
    print(z)


default_image_binary = b64encode(z).decode("utf-8")

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
	binaire = models.TextField(default=default_image_binary,null=True)

	def __str__(self):
		return self.user.username
	

