from django.shortcuts import render, redirect
from .models import LoginUser
from global_session import GlobalSession

# Create your views here.
def index (request):
    
    error = False
    blank = False
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username != '' and password != '':
            user = LoginUser.objects.filter(username=username, password=password)
            if user:
                request.session['username'] = user[0].username
                request.session['firstname'] = user[0].firstname
                request.session['middlename'] = user[0].middlename
                request.session['lastname'] = user[0].lastname
                request.session['userid'] = user[0].userid
                request.session['usertype'] = user[0].usertype
                return redirect('home')
            else:
                error = True
        else:
            blank = True
            
        return render(request, 'pages/login.html', {'error': error, 'blank': blank})
    else:
        if 'username' in request.session and request.session['username'] is not None:
            return redirect('home')
        else:
            return render(request, 'pages/login.html', {'error': error, 'blank': blank})
        
def add_student (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/add_student.html', { 'details': details })
    else:
        return redirect('/')

def add_instructor (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/add_instructor.html', { 'details': details })
    else:
        return redirect('/')
    
def change_password (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/change_password.html', { 'details': details })
    else:
        return redirect('/')

def logout (request):
    request.session.flush()
    return redirect('/')