from django.shortcuts import render ,redirect
from django.http import Http404,HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth.decorators import login_required





from .mock_cours import *

def all_cours(request):
	return render(request,'cours.html',{'cours':listes_de_cours})






@login_required
def do_cours(request,nom,id):
	partie=0
	for i in listes_de_cours:
		if i['id_nom']==nom:
			for j in i['contenu']:
				if j['id']== id:
					pere=i
					partie = j

	return render(request,'faire_cours.html',{'cours':pere['contenu'],'this':partie,'pere':pere})
"""
def general_this_cours(request,nom):
	partie=0
	nom = nom.upper()
	print(nom)
	for i in listes_de_cours:
		if i['id_nom'] == nom :
			return HttpResponseRedirect(reverse('partie_cours',kwargs={'nom':nom,'id': 1}))
	raise Http404("Page non trouvé ouloulouh")

	"""