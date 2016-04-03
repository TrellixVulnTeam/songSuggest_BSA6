from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")
def main(request):
	# username = request.POST['username']
 #    password = request.POST['password']
 #    user = authenticate(username=username, password=password)
 #    if user is not None:
 #        if user.is_active:
 #            login(request, user)
 #            # Redirect to a success page.
 #        else:
 #            # Return a 'disabled account' error message
 #    else:
 #        # Return an 'invalid login' error message.
	return render(request, "main/main.html", {}) #searches in firstapp/templates/firstapp/page2.html

# Create your views here.
