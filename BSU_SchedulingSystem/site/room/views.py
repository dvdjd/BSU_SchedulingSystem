from django.shortcuts import render, redirect

# Create your views here.
def room (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/room.html')
    else:
        return redirect('/')