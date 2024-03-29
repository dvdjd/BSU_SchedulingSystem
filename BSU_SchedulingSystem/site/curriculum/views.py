from django.shortcuts import render, redirect
from .models import CourseModel, AcademicProgramModel, SectionModel, SubjectModel, InstructorModel, SubjectScheduleModel
from room.models import RoomModel
from pages.models import FacultyModel
from student.models import StudentModel, StudentScheduleModel
from loginuser.models import LoginUser
from global_session import GlobalSession
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json, datetime
from django.db.models import Q

# Create your views here.
def curriculum (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        programs = AcademicProgramModel.objects.all()
        return render(request, 'pages/curriculum.html', {'request': request, 'details': details, 'programs': programs })
    else:
        return redirect('/')
    
def generate_schedule (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        programs = AcademicProgramModel.objects.all()
        sections = SectionModel.objects.all()
        return render(request, 'pages/generate_schedule.html', {'request': request, 'details': details, 'sections': sections})
    else:
        return redirect('/')

def search_schedule (request):
    if request.method == 'POST':
        subjects = SubjectScheduleModel.objects.filter(Q(academic_year=request.POST.get('year')) & Q(semester=request.POST.get('semester')) & Q(section=request.POST.get('section')))
        subject_dict = serializers.serialize('python', subjects)
        return JsonResponse({ 'subjects': subject_dict })
    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            programs = AcademicProgramModel.objects.all()
            sections = SectionModel.objects.all()
            return render(request, 'pages/search_schedule.html', {'request': request, 'details': details, 'sections': sections})
        else:
            return redirect('/')

def delete_schedule  (request):
    if request.method == 'POST':
        subjects = SubjectScheduleModel.objects.filter(Q(academic_year=request.POST.get('year')) & Q(semester=request.POST.get('semester')) & Q(section=request.POST.get('section')))
        subjects.delete()
        return HttpResponse('success')

def add_subject (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        programs = AcademicProgramModel.objects.all()
        sections = SectionModel.objects.all()
        subjects = SubjectModel.objects.all()
        rooms = RoomModel.objects.all()
        return render(request, 'pages/add_subject.html', {'request': request, 'details': details, 'programs': programs, 'sections': sections, 'subjects': subjects, 'rooms': rooms })
    else:
        return redirect('/')
    
def add_schedule (request):
    
    if request.method == 'POST':
        if request.POST.get('type') == 'fulltime':
            instructor = InstructorModel(instructor_id=request.POST.get('instructor_id'), first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), type=request.POST.get('type'), college=request.POST.get('college'), academic_year=request.POST.get('year'), section=request.POST.get('section'), semester=request.POST.get('semester'), subject_code=request.POST.get('subject_code'), units=request.POST.get('units'), room=request.POST.get('room'), campus=request.POST.get('campus'))
        else:
            instructor = InstructorModel(instructor_id=request.POST.get('instructor_id'), first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), type=request.POST.get('type'), college=request.POST.get('college'), days=request.POST.get('days'), time_in=request.POST.get('time_in'), time_out=request.POST.get('time_out'), academic_year=request.POST.get('year'), section=request.POST.get('section'), semester=request.POST.get('semester'), subject_code=request.POST.get('subject_code'), units=request.POST.get('units'), room=request.POST.get('room'), campus=request.POST.get('campus'))
        
        instructor.save()
        return HttpResponse('success')
    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            instructors = InstructorModel.objects.all()
            programs = AcademicProgramModel.objects.all()
            sections = SectionModel.objects.all()
            subjects = SubjectModel.objects.all()
            rooms = RoomModel.objects.all()
            return render(request, 'pages/add_schedule.html', { 'request': request, 'details': details, 'instructors': instructors, 'programs': programs, 'sections': sections, 'subjects': subjects, 'rooms': rooms })
        else:
            return redirect('/')
    
def populate_name (request):
    if request.method == 'POST':
        instructors = LoginUser.objects.filter(userid=request.POST.get('userid'))
        
        instructor_dict = serializers.serialize('python', instructors)
        return JsonResponse({ 'instructor': instructor_dict })
    else:
        return HttpResponse('this is get')
    
def populate_programcode (request):
    if request.method == 'POST':
        course = CourseModel.objects.filter(course_code=request.POST.get('course_code'))
        return HttpResponse(course[0].program_code)
    else:
        return HttpResponse('this is get')

def save_schedule (request):
    if request.method == 'POST':
        program = SubjectScheduleModel(profesor=request.POST.get('profesor'), days=request.POST.get('day'), start=request.POST.get('start'), end=request.POST.get('end'), subject_code=request.POST.get('subject'), academic_year=request.POST.get('year'), section=request.POST.get('section'), semester=request.POST.get('semester'), units=request.POST.get('units'))
        program.save()
        return HttpResponse('success')
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
    
def add_instructor_schedule (request):
    if request.method == 'POST':
        day_sched = json.loads(request.POST.get('days'))
        for day in day_sched:
            schedules = FacultyModel(instructor_id=request.POST.get('userid'), subject_code=request.POST.get('subject'), room=request.POST.get('room'), course_code=request.POST.get('course'), program_code=request.POST.get('program'), section_code=request.POST.get('section'), days=day, time_in=request.POST.get('time_in'), time_out=request.POST.get('time_out'))
            schedules.save()
        return HttpResponse(day_sched)
    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            schedules = FacultyModel.objects.filter(instructor_id=request.GET.get('instructor_id'))
            user = LoginUser.objects.filter(userid=request.GET.get('instructor_id'))
            sections = SectionModel.objects.all()
            subjects = SubjectModel.objects.all()
            rooms = RoomModel.objects.all()
            courses = CourseModel.objects.all()
            students = StudentModel.objects.filter(status='irregular')
            return render(request, 'pages/add_instructor_schedule.html', {'request': request, 'details': details, 'schedules': schedules, 'instructors': user, 'courses': courses, 'sections': sections, 'subjects': subjects, 'rooms': rooms, 'students': students})
        else:
            return redirect('/')
        
def get_schedule (request):
    if request.method == 'POST':
        schedule = FacultyModel.objects.filter(id=request.POST.get('id'))
        
        schedule_dict = serializers.serialize('python', schedule)
        return JsonResponse({ 'schedule': schedule_dict })
    
def update_instructor_schedule (request):
    if request.method == 'POST':
        schedule = FacultyModel.objects.get(id=request.POST.get('id'))
        schedule.subject_code = request.POST.get('subject')
        schedule.course_code = request.POST.get('course')
        schedule.program_code = request.POST.get('program')
        schedule.section_code = request.POST.get('section')
        schedule.room = request.POST.get('room')
        schedule.days = request.POST.get('days')
        schedule.time_in = request.POST.get('time_in')
        schedule.time_out= request.POST.get('time_out')
        schedule.save()
        return HttpResponse('success')
    
def delete_instructor_schedule (request):
    if request.method == 'POST':
        schedule = FacultyModel.objects.get(id=request.POST.get('id'))
        schedule.delete()
        return HttpResponse('success')

def add_student_schedule (request):
    if request.method == 'POST':
        day_sched = json.loads(request.POST.get('days'))
        for day in day_sched:
            schedules = FacultyModel(instructor_id=request.POST.get('userid'), subject_code=request.POST.get('subject'), room=request.POST.get('room'), course_code=request.POST.get('course'), program_code=request.POST.get('program'), section_code=request.POST.get('section'), days=day, time_in=request.POST.get('time_in'), time_out=request.POST.get('time_out'))
            schedules.save()
        return HttpResponse(day_sched)
    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            student = StudentModel.objects.filter(student_id=request.GET.get('student_id')).first()
            users = LoginUser.objects.filter(userid=request.GET.get('student_id'))
            
            if student.status == 'regular':
                schedules = FacultyModel.objects.filter(section_code=student.section_code)
            else:
                schedules = []
                irreg_scheds = StudentScheduleModel.objects.filter(student_id=request.GET.get('student_id'))
                
                for sched in irreg_scheds:
                    faculty_sched = FacultyModel.objects.filter(id=sched.faculty_schedule_id).first()
                    schedules.append({
                        'id': sched.id,
                        'subject_code': faculty_sched.subject_code,
                        'room': faculty_sched.room,
                        'section_code': faculty_sched.section_code,
                        'days': faculty_sched.days,
                        'time_in': faculty_sched.time_in,
                        'time_out': faculty_sched.time_out,
                    })
                
            
            return render(request, 'pages/add_student_schedule.html', {'request': request, 'details': details, 'schedules': schedules, 'student': student, 'users': users })
        else:
            return redirect('/')

def populate_irreg_student (request):
    if request.method == 'POST':
        students = StudentModel.objects.filter(student_id=request.POST.get('student_id'))
        student_details = []
        
        for student in students:
            user = LoginUser.objects.filter(userid=student.student_id).first()
            student_details.append({
                'firstname': user.firstname,
                'lastname': user.lastname,
                'level': student.level,
                'course': student.course_code,
                'program': student.program_code,
                'section': student.section_code
            })
        return JsonResponse(student_details, safe=False)
    
def save_irreg_student (request):
    if request.method == 'POST':
        schedule = StudentScheduleModel(student_id=request.POST.get('student_id'), faculty_schedule_id=request.POST.get('sched_id'))
        schedule.save()
        
        return HttpResponse('success')

def delete_student_schedule (request):
    if request.method == 'POST':
        schedule = StudentScheduleModel.objects.get(id=request.POST.get('id'))
        schedule.delete()
        
        return HttpResponse('success')

def populate_subject (request):
    if request.method == 'POST':
        subject = SubjectModel.objects.filter(subject_code=request.POST.get('subject_code'))
        return HttpResponse(subject[0].subject_description)
    else:
        return HttpResponse('this is get')

def get_subjects (request):
    if request.method == 'POST':
        subjects = InstructorModel.objects.filter(Q(academic_year=request.POST.get('year')) & Q(semester=request.POST.get('semester')) & Q(section=request.POST.get('section')))
        subject_dict = serializers.serialize('python', subjects)
        return JsonResponse({ 'subjects': subject_dict })

def delete_subject (request):
    if request.method == 'POST':
        schedule = InstructorModel.objects.get(id=request.POST.get('id'))
        schedule.delete()
        
        return HttpResponse('success')