from django.shortcuts import render, redirect
from global_session import GlobalSession

# Create your views here.
def course_offer (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/course_offer.html', {'request': request, 'details': details})
    else:
        return redirect('/')
    
def course_schedule (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/course_schedule.html', {'request': request, 'details': details})
    else:
        return redirect('/')