from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")
def main(request):
	return render(request, "main/main.html", {}) #searches in firstapp/templates/firstapp/page2.html

# Create your views here.
