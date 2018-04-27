from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import People
def index(request):
	people = People.objects.all()
	return render_to_response("hsuan/menu.html",locals())
# Create your views here.
