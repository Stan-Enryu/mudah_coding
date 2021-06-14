from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from .forms import (
RegisterForm,
SettingForm, 
ProfileForm,
 )

from .models import Profile
import datetime
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
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Berhasil buat akun')
			return redirect('login')
	else:
		form = RegisterForm()
	context = {'form': form}    
	return render(request, 'users/register.html', context)

def LogoutUser(request):
	if request.user.is_authenticated:
		logout(request)
		messages.info(request, 'Berhasil Logout')
	return redirect('home')

@login_required
def Edit_Profile(request):

	if request.method == 'POST':
		
		p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

		# mengecek datanya valid dan 
		if p_form.is_valid():
			p_form.save()
			messages.success(request, f'Akun kamu berhasil diupdate')
			return redirect('profile')

	else:
		p_form = ProfileForm(instance=request.user.profile)

	context = {
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)

@login_required
def Setting(request):
	if request.method == 'POST':
		form = SettingForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, f'Password berhasil diupdate')
			return redirect('setting')
		else:
			messages.success(request, f'Password tidak berhasil diupdate')
			return redirect('setting')
	else:
		form = SettingForm(request.user)

	is_premium = Group.objects.get(name='Premium') in request.user.groups.all()

	context = {
		'form': form,
		'is_premium': is_premium,
	}
	return render(request, 'users/setting.html', context)

@login_required
def Upgrade_Account(request):
	
	if request.GET.get('buy') == 'buy':
		if request.user.is_authenticated:
			my_group = Group.objects.get(name='Premium') 

			if my_group not in request.user.groups.all():
				my_group.user_set.add(request.user)

				date_premium_now = datetime.datetime.now().date()
				date_premium_now += datetime.timedelta(days=30)

				Profile.objects.filter(pk=request.user.profile.id).update(date_premium=date_premium_now)
			else:
				my_group.user_set.remove(request.user)
		else:
			return redirect('login')
