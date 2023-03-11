from django.shortcuts import render, redirect
from global_session import GlobalSession
from curriculum.models import CourseModel

# Create your views here.
def course_offer (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        courses = CourseModel.objects.all()
        return render(request, 'pages/course_offer.html', {'request': request, 'details': details, 'courses': courses })
    else:
        return redirect('/')
    
def course_offering (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        course = CourseModel.objects.filter(course_code=request.GET.get('course_code'))
        return render(request, 'pages/course_offering.html', {'request': request, 'details': details, 'course': course})
    else:
        return redirect('/')   
    
def course_schedule (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/course_schedule.html', {'request': request, 'details': details})
    else:
        return redirect('/')