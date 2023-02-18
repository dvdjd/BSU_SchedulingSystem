from django.shortcuts import render, redirect

def home (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/home.html')
    else:
        return redirect('/')
    
def faculty (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/faculty.html')
    else:
        return redirect('/')