from django.shortcuts import render, redirect

# Create your views here.
def student (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/student.html')
    else:
        return redirect('/')