from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")
def login(request):
	return render(request, "login/login.html", {}) #searches in firstapp/templates/firstapp/page2.html

# Create your views here.
