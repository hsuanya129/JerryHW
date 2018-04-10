from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello mom I'm here")

# Create your views here.
