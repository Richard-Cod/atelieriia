from django.shortcuts import render , get_object_or_404 ,redirect,HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import Profile
from .forms import UserForm,My_own_userForm


from django.contrib.auth.decorators import login_required


from .mock_bureau import membres_bureau

from base64 import b64encode

default_image_binary = "iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAM1BMVEX+///9/v74+fn3+Pjy8/Tu7+/t7u/p6urn6On6+/vs7e37/Pzx8vLq6+z19vbv8PH09fVYJh4NAAAEGklEQVR42u2dC3ajMAxFDRgscPjsf7UNbXPazkzaNOg9CY/vDt7RXzJJqFQqlUqlUnmEpu1i7Id3+hi7tgkno+nikOQfpCF2p1Ezxkm+ZYpjcE++zPIA8yUHz3SDPMzQBa8sX43xs1mW4JHuVcYvpfizSh7kKQZnsRLlWVIMfriZ4+xGaZMcIrXBBYscxkX6WkWBNZijosOBEiUd5krUdIiYpmGFOHcR8a2oYtbc5ySqzFYj1yDK9MGETdQxaYa1HWsnWTiXumMZVRPljHWD3z/OAmEIZFRLoaVJQAahmwQUITvcebEXGNTElQUHtZZEAcLsgmGhTu64RoHC8y2oZzF9axIotLzVCJY5kOgEDKsmgkOEFySQSeQzl8ABMBqaNI7I/uSNFCgAO19uSQRsT2ymK3jSYq2FgLMId6ENz74FCeF0W/AywiokgqcKqUJAVCFVCIgq5P8siIQWpZheqwrxNlgVMyFyhMAXjazlA2GLEiigd9jXzxkCB3hFZN2s4PmXk31DuAgYzlqLsGpkvQmEp63AQrBwel/CMZR151F9tmwZ68DHWtxbKPpmRbtOo9+icDbYhCBhHafhQcILEWwDzGp94ZWEV0XAfSOvimCfnpEeC+ATMGuogidgZvKFrlI4CxT84M72LJhvsT0LlrfongXKW8yGEVoTudUQN5SwqyFsT8fts4C9PGuh9ZVGvZRwO3hgKeEXEUy4U7/lQYa7RRGBhDtzWEdWd97KF3xgsKjqiAzMXDBCGy6r3Kudge1yr3JRZB1A0SaxNoiaSeyKobJJDIuhap9ibxClY7UDg6hEiQeDqESJC4MomMSHQRRM4sQgh03ixSB7E3zuoq708NS6y1K78rqJkNcoKSFCdkbvj5XxawjbCVdx5vXlWdfW8Yy7E9W85Spn7STvL0rB85W3WL8KOd+eVFWIP4uUEiPNuc6GgFPJFnzRn+0Aqj/t+moah/PdpPUvV44mxDGd9uamqUOSkxTcHj4kJtuzm0Z8+ImTrHJVuOYuW/dq4mG3+jCK4Z5uUX35kIykNJuqDCsp46rnVJ9ZqbHSbMDvR+aNtI/IC/xH6Ca8lhFpC9ZfDTbLqh7e34b+uugbpukuJFP8YZiL4h9aZiMRH2IULDOS3eke87o9HzNt7DG14tmY6WP7xB+YKjWD2gy/yWatD3e672YPGSZH1yretcT8k4zDzzFYrLkIGd9LUZySKNz5u9FsWvWeY8r6Ox0b/t4kLafUsW+S1F4uWDOi/7eNRcqcXz7AMyk9t7InluBYb851/LGVD1aF528+aPTW6bZs509Zb0wqz489kPW/irRhKSFn7axlhMg1SPC/VUhC6YMce9pyhJy8YbwRyxFSRPa95l+dzwjtGaoQZxQkRAqhCvFGFeKNKsQbL26/cd+lwF+LAAAAAElFTkSuQmCC"



def accueil(request):
	return render(request,'index.html',{})



def messages(request):
	return render(request,'messages.html',{})


def test(request):
	form = My_own_userForm
	return render(request,'test.html',{'form':form})


def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request,new_user)
			return redirect('profile')
	else:
		form = UserForm()
	return render(request,'registration/signup.html',{'form':form})

@login_required
def profile(request):
	profile = Profile.objects.filter(user=request.user) or None
	if request.method == 'POST':
		if Profile.objects.filter(user=request.user).exists():
			form = My_own_userForm(request.POST,request.FILES or None,instance=profile[0])
		else:
			form = My_own_userForm(request.POST,request.FILES or None)
	  
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			if 'avatar' in request.FILES:
				img_recu =request.FILES['avatar']
				image = b64encode(img_recu.read()).decode("utf-8")
				post.binaire= image

			if 'avatar-clear' in request.POST:
				post.binaire = default_image_binary
		
			

			post.save()
			return redirect('accueil')

	else:
		if profile:
			form = My_own_userForm(instance=profile[0])
		else:
			form=My_own_userForm()
		

	return render(request,'registration/profile.html',{'form':form})





def bureau(request):
	return render(request,'bureau.html',{})

def about(request):
	return render(request,'about.html',{'membres_bureau':membres_bureau})