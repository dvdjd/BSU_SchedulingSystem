from django.shortcuts import render, redirect
from global_session import GlobalSession
from curriculum.models import CourseModel, CurriculumYearModel, SectionModel, CurriculumModel, SubjectModel
from django.db.models import Q
from django.http import JsonResponse, HttpResponse

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
        courses = CourseModel.objects.all()
        subjects = SubjectModel.objects.all()
        years = CurriculumYearModel.objects.all()
        sections = SectionModel.objects.all()
        
        course = CourseModel.objects.filter(course_code=request.GET.get('course_code'))
        curriculums = CurriculumModel.objects.filter(course_code__course_code=request.GET.get('course_code'))
        
        course_curriculum = []
        
        for curriculum in curriculums:
            subject = SubjectModel.objects.filter(subject_code=curriculum.subject_code).first()
            course_curriculum.append({
                'subject_code': curriculum.subject_code,
                'subject_name': subject.subject_description,
                'lecture': curriculum.lecture,
                'lab': curriculum.lab,
                'units': curriculum.units,
            })
            
        return render(request, 'pages/course_offering.html', {'request': request, 'details': details, 'course': course, 'years': years, 'sections': sections, 'curriculums': course_curriculum, 'courses': courses, 'subjects': subjects })
    else:
        return redirect('/')   
    
def course_schedule (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/course_schedule.html', {'request': request, 'details': details})
    else:
        return redirect('/')
    
def search_course (request):
    if request.method == 'POST':
        curriculums = CurriculumModel.objects.filter(Q(curriculum_year=request.POST.get('year')) & Q(level=request.POST.get('level')) & Q(period=request.POST.get('period')))
        
        course_curriculum = []
                
        for curriculum in curriculums:
            subject = SubjectModel.objects.filter(subject_code=curriculum.subject_code).first()
            course_curriculum.append({
                'subject_code': curriculum.subject_code.subject_code,
                'subject_name': subject.subject_description,
                'lecture': curriculum.lecture,
                'lab': curriculum.lab,
                'units': curriculum.units,
            })
                
        return JsonResponse(course_curriculum, safe=False)
    
def save_course_offering (request):
    if request.method == 'POST':
        year = CurriculumYearModel.objects.get(curriculum_year=request.POST.get('year'))
        course = CourseModel.objects.get(course_code=request.POST.get('course_code'))
        subject = SubjectModel.objects.get(subject_code=request.POST.get('subject_code'))
        curriculum = CurriculumModel(
            curriculum_year=year, 
            period=request.POST.get('period'), 
            level=request.POST.get('level'), 
            course_code=course, 
            subject_code=subject, 
            program_code=request.POST.get('program_code'), 
            lecture=request.POST.get('lecture'), 
            lab=request.POST.get('lab'), 
            units=request.POST.get('units')
        )
        curriculum.save()
        return HttpResponse('success')
    else:
        return HttpResponse('this is get')