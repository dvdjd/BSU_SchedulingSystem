from django.shortcuts import render, redirect
from .models import CourseModel, AcademicProgramModel
from global_session import GlobalSession
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
def curriculum (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        programs = AcademicProgramModel.objects.all()

        return render(request, 'pages/curriculum.html', {'request': request, 'details': details, 'programs': programs})
    else:
        return redirect('/')
    
def add_schedule (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/add_schedule.html', {'request': request, 'details': details})
    else:
        return redirect('/')
    
def populate_programcode (request):
    if request.method == 'POST':
        course = CourseModel.objects.filter(course_code=request.POST.get('course_code'))
        return HttpResponse(course[0].program_code)
    else:
        return HttpResponse('this is get')
    
def save_curriculum (request):
    if request.method == 'POST':
        program = AcademicProgramModel(program_code=request.POST.get('program_code'), program_description=request.POST.get('program_description'))
        program.save()
        return HttpResponse('success')
    else:
        return HttpResponse('this is get')
    
def get_curriculum (request):
    if request.method == 'POST':
        program = AcademicProgramModel.objects.filter(program_code=request.POST.get('program_code'))
        program_dict = serializers.serialize('python', program)
        return JsonResponse({ 'program': program_dict })
    else:
        return HttpResponse('this is get')
    
def update_curriculum (request):
    if request.method == 'POST':
        program = AcademicProgramModel.objects.get(program_code=request.POST.get('program_code'))
        program.program_description = request.POST.get('program_description')
        program.save()
        return HttpResponse('success')
    else:
        return HttpResponse('this is get')