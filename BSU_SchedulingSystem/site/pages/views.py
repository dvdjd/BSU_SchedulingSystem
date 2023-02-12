from django.shortcuts import render
from django.http import HttpResponseRedirect



def home (request):
    if request.user.is_authenticated:
        return render(request, 'pages/home.html')
    else:
        return HttpResponseRedirect('/')