from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
import kitchenAPI

@login_required
def userKitchen(request, user_name):
	context = RequestContext(request, {
#		'all_ingredient_list': kitchenAPI.getKitchenIngredientList(user_name)
		'all_ingredient_list': [],
		'user_name': user_name,
	})
	return render_to_response('kitchen/userKitchen.html', context)
