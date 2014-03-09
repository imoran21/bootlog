
##HOME APP

from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from forms import UserForm, BillForm, BillLineForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.forms.models import formset_factory, inlineformset_factory
from home.models import Bill, BillLine

import string
import random
def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def home_base(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		print form.is_valid()
		new_user_a = authenticate(username=request.POST['username'], password=request.POST['password'])
		login(request, new_user_a)
		
		return redirect('logged_in')
	else:
		form = UserForm()
		return render(request, 'home/home_base.html', {'form':form})



def logged_in(request):
	if request.user.is_authenticated():
		form = BillForm()
		return render(request, 'home/logged_in.html', {'u': request.user, 'form':form})
	else:
		return redirect('home_base')

def logout_view(request):
	logout(request)
	return redirect('home_base')


def create_bill(request):
	if request.method == "POST":
		b = BillForm(request.POST.copy())
		if b.is_valid():
			b.save()
			return render_to_response('home/logged_in.html', {'u': request.user}, context_instance=RequestContext(request))

		else:
			form = BillForm(request.POST)
			return render(request, 'home/create_bill.html', {'form':form})

	else:
		form = BillForm(request.POST)
		return render(request, 'home/create_bill.html', {'form':form})


def create_bill_line(request):
	if request.method == "POST":
		b = BillForm(request.POST.copy())
		if b.is_valid():
			BillLineFormSet = formset_factory(BillLineForm, extra = 3)
			b = b.save()
			bl =BillLineFormSet()
			return render(request, 'home/create_bill_line.html', {'formset':bl, 'inv_num':b.inv_num})


		else:
			return redirect('create_bill')
	else:
		return redirect('create_bill')




