from django.shortcuts import render, redirect
from .models import CourseModel
from global_session import GlobalSession
from django.http import HttpResponse

# Create your views here.
def curriculum (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/curriculum.html', {'request': request, 'details': details})
    else:
        return redirect('/')
    
def populate_programcode (request):
    if request.method == 'POST':
        course = CourseModel.objects.filter(course_code=request.POST.get('course_code'))
        return HttpResponse(course[0].program_code)
    else:
        return HttpResponse('this is get')