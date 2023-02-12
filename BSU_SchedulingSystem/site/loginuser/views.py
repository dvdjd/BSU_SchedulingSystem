from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import LoginUser

# Create your views here.
def index (request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username != '' and password != '':
            user = LoginUser.objects.filter(username=username, password=password)
            if user:
                return HttpResponseRedirect('home')
            else:
                error = True
                return render(request, 'pages/login.html', {'error': error})
        else:
            blank = True
            return render(request, 'pages/login.html', {'blank': blank})
    else:
        return render(request, 'pages/login.html')