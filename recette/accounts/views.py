from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/register.html', {
		'form': form
	})
	
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login_django(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Invalid login information.')
	else:
		context = {}
		context.update(csrf(request))
		return render_to_response('accounts/login.html', context)
		
def logout(request):
	logout_django(request)
	return HttpResponseRedirect('/')

	