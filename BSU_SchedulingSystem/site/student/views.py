from django.shortcuts import render, redirect
from global_session import GlobalSession

# Create your views here.
def student (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/student.html', {'request': request, 'details': details})
    else:
        return redirect('/')