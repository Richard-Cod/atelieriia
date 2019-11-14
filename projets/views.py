from django.shortcuts import render ,redirect
from django.http import Http404,HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .mock_projets import *



def projets(request):
	return render(request,'projets.html',{'projets':projets_data})