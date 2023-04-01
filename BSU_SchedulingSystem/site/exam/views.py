from django.shortcuts import render, redirect
from global_session import GlobalSession
from curriculum.models import AcademicProgramModel, SectionModel, SubjectModel, CourseModel
from room.models import RoomModel
from .models import ExamModel
from loginuser.models import LoginUser
from django.http import HttpResponse, JsonResponse

# Create your views here.
def exam (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        program_codes = AcademicProgramModel.objects.all()
        sections = SectionModel.objects.all()
        exams = ExamModel.objects.all()
        rooms = RoomModel.objects.all()
        subjects = SubjectModel.objects.all()
        courses = CourseModel.objects.all()
        
        exam_schedules = []
        
        for exam in exams:
            subject = SubjectModel.objects.filter(subject_code=exam.subject_code).first()
            course = CourseModel.objects.filter(course_code=exam.course_code).first()
            section = SectionModel.objects.filter(section_code=exam.section_code).first()
            level = ''
            if section.level == '1':
                level = '1st Year'
            elif section.level == '2':
                level = '2nd Year'
            elif section.level == '3':
                level = '3rd Year'
            elif section.level == '4':
                level = '4th Year'
                
            exam_schedules.append({
                'id': exam.id,
                'program_code': course.program_code,
                'course': course.course_name,
                'section': exam.section_code,
                'level': level,
                'subject_code': subject.subject_code,
                'subject_description': subject.subject_description,
                'schedule': exam.days.capitalize() + ' ' + exam.time_in.strftime('%I:%M %p') + '-' + exam.time_out.strftime('%I:%M %p')
            })
        return render(request, 'pages/exam.html', {'request': request, 'details': details, 'program_codes': program_codes, 'sections': sections, 'exam_schedules': exam_schedules, 'rooms': rooms, 'subjects': subjects, 'courses': courses })
    else:
        return redirect('/')
    
def add_exam_schedule (request):
    if request.method == 'POST':
        exam = ExamModel(subject_code=request.POST.get('subject'), course_code=request.POST.get('course'), section_code=request.POST.get('section'), instructor_id=request.POST.get('userid'), room=request.POST.get('room'), days=request.POST.get('days'), time_in=request.POST.get('time_in'), time_out=request.POST.get('time_out'))
        exam.save()
        return HttpResponse('success')
    
def modify_exam_schedule (request):
    if request.method == 'POST':
        exams = ExamModel.objects.filter(id=request.POST.get('id'))
        
        exam_schedule = []
        
        for exam in exams:
            user = LoginUser.objects.filter(userid=exam.instructor_id).first()
            course = CourseModel.objects.filter(course_code=exam.course_code).first()
            exam_schedule.append({
                'id': exam.id,
                'instructor_id': exam.instructor_id,
                'first_name': user.firstname,
                'last_name': user.lastname,
                'course_code': exam.course_code,
                'program_code': course.program_code.program_code,
                'section_code': exam.section_code,
                'subject_code': exam.subject_code,
                'room': exam.room,
                'days': exam.days,
                'time_in': exam.time_in,
                'time_out': exam.time_out
            })
            
        
        return JsonResponse(exam_schedule, safe=False)

def save_exam_schedule (request):
    if request.method == 'POST':
        exam = ExamModel.objects.get(id=request.POST.get('id'))
        exam.subject_code = request.POST.get('subject')
        exam.course_code = request.POST.get('course')
        exam.section_code = request.POST.get('section')
        exam.room = request.POST.get('room')
        exam.days = request.POST.get('days')
        exam.time_in = request.POST.get('time_in')
        exam.time_out= request.POST.get('time_out')
        exam.save()
        return HttpResponse('success')
    
def delete_exam_schedule (request):
    if request.method == 'POST':
        exam = ExamModel.objects.get(id=request.POST.get('id'))
        exam.delete()
        return HttpResponse('success')