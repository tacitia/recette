from django.template import RequestContext
from django.shortcuts import render, render_to_response

def index(request):
	context = RequestContext(request, {})
	return render_to_response('homepage/base.html', context)