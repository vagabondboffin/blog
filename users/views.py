from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'You are now able to log in!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form' : form})

# def login_user(request):
# 	return render(request, 'users/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("you logged out!"))
	return redirect('login')

@login_required
def profile(request):
	return render(request, 'users/profile.html')
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error