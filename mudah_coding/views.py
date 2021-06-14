from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from users.models import Profile
from users.views import Upgrade_Account

class HomeView(TemplateView):
	template_name = 'home.html'

def pricing(request):
	
	Upgrade_Account(request)
		
	return render(request, 'pricing/pricing.html')
