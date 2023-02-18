from django.shortcuts import render, redirect

# Create your views here.
def exam (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/exam.html')
    else:
        return redirect('/')