from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from users.models import Profile

from django.utils import timezone
import datetime

class HomeView(TemplateView):
	template_name = 'home.html'

def pricing(request):
	
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
			
		
	return render(request, 'pricing/pricing.html')
