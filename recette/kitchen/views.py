from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django import forms
from django.utils import simplejson
import kitchenAPI


@login_required
@csrf_protect

def userKitchen(request):
	ingredientList = kitchenAPI.getKitchenIngredientList(request.user)
	context = RequestContext(request, {
		'all_ingredient_list': kitchenAPI.getKitchenIngredientList(request.user),
		'user':request.user,
		'all_ingredient_Names': kitchenAPI.getAllIngredientNames(),
	})
	return render_to_response('kitchen/userKitchen.html', context)

class CreateIngredientForm(forms.Form):
     ingredientName = forms.CharField()
     ingredientType = forms.CharField()
     basicMeasure = forms.CharField()
     brand = forms.CharField()
     defaultAmount = forms.FloatField()

def createIngredient(request):
	if request.method == 'GET':
		context = RequestContext(request, {
				'user':request.user,
		})
		return render_to_response('kitchen/createIngredient.html',context)
	if request.method == 'POST':
		ciForm = CreateIngredientForm(request.POST)
		if ciForm.is_valid():
			print "valid form"
			kitchenAPI.createIngredient(ciForm.cleaned_data['ingredientName'],
					 ciForm.cleaned_data['basicMeasure'],
					 ciForm.cleaned_data['ingredientType'],
					 ciForm.cleaned_data['brand'],
					 int(ciForm.cleaned_data['defaultAmount']*100))
			return HttpResponseRedirect('seccess/') 

def success(request):
	return HttpResponse("seccess")

def addIngredientAmount(request):
	if request.is_ajax():
		print('AJAX!!!')
		if request.method == 'POST':
			print request.body
			print "PRINT...."
			json_data = simplejson.loads(request.body)
			try:
				print json_data['ingredientID']
				print json_data['amountAdd']
				kitchenAPI.increaseIngredientAmount(currentUser = request.user,ingredientID = json_data['ingredientID'],amount = int(float(json_data['amountAdd'])*100))
			except KeyError:
				HttpResponseServerError("Malformed data!")
	return HttpResponseRedirect('/kitchen/')

def addNewIngredient(request):
	if request.is_ajax():
		print('AJAX!!!')
		if request.method == 'POST':
			print request.body
			print "PRINT...."
			json_data = simplejson.loads(request.body)
			try:
				print json_data['ingredientName']
				print json_data['amount']
				kitchenAPI.addIngredient(currentUser = request.user,ingredientName = json_data['ingredientName'],amount = int(float(json_data['amount'])*100))
			except KeyError:
				HttpResponseServerError("Malformed data!")
	return HttpResponseRedirect('/kitchen/')
