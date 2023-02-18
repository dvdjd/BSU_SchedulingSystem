from django.shortcuts import render, redirect

# Create your views here.
def curriculum (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/curriculum.html')
    else:
        return redirect('/')