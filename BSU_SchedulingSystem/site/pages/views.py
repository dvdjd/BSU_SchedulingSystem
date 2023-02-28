from django.shortcuts import render, redirect
from global_session import GlobalSession

def home (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/home.html', {'details': details})
    else:
        return redirect('/')
    
def faculty (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/faculty.html', {'details': details})
    else:
        return redirect('/')