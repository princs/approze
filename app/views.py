from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
	template_name = 'index.html'
	return render (request, template_name)

