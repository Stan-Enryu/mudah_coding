from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from .forms import (
UserRegisterForm,
UserUpdateForm, 
ProfileUpdateForm,
 )
from django.contrib.auth import authenticate, login, logout

def LoginUser(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.info(request, f'Selamat datang {request.user}')
			return redirect('home')
		else:
			messages.info(request, 'Username atau password salah')

	context = {}
	return render(request, 'users/login.html', context)

def RegisterUser(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Berhasil buat akun')
			return redirect('login')
	else:
		form = UserRegisterForm()
	context = {'form': form}    
	return render(request, 'users/register.html', context)

def LogoutUser(request):
	if request.user.is_authenticated:
		logout(request)
		messages.info(request, 'Berhasil Logout')
	return redirect('home')

@login_required
def profile_edit(request):
	if request.method == 'POST':
		
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if p_form.is_valid():
			p_form.save()
			messages.success(request, f'Akun kamu berhasil diupdate')
			return redirect('profile')
	else:
		
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)

@login_required
def setting(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(data=request.POST, user=request.user)
		if u_form.is_valid():
			u_form.save()
			update_session_auth_hash(request, u_form.user)
			messages.success(request, f'Password berhasil diupdate')
			return redirect('setting')
		else:
			messages.success(request, f'Password tidak berhasil diupdate')
			return redirect('setting')
	else:
		u_form = UserUpdateForm(request.user)

	is_premium = Group.objects.get(name='Premium') in request.user.groups.all()

	context = {
		'u_form': u_form,
		'is_premium': is_premium,
	}
	return render(request, 'users/setting.html', context)
