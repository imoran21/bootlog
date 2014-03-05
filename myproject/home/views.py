from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
def home_base(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		print form.is_valid()
		new_user_a = authenticate(username=request.POST['username'], password=request.POST['password'])
		print new_user_a
		
		return render(request, 'home/logged_in.html', {'u': new_user_a})
	else:
		form = UserForm()
		return render(request, 'home/home_base.html', {'form':form})



def logged_in(request):
	if request.user.is_authenticated():
		return render(request, 'home/logged_in.html', {'u': request.user})
	else:
		return redirect('home_base')

def logout_view(request):
	logout(request)
	return redirect('home_base')

