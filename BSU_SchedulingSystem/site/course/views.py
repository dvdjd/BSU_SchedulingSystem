from django.shortcuts import render, redirect

# Create your views here.
def course_offer (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/course_offer.html')
    else:
        return redirect('/')
    
def course_schedule (request):
    if 'username' in request.session and request.session['username'] is not None:
        return render(request, 'pages/course_schedule.html')
    else:
        return redirect('/')