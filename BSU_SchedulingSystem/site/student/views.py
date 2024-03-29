from django.shortcuts import render, redirect
from global_session import GlobalSession
from pages.models import FacultyModel
from student.models import StudentModel, StudentScheduleModel
from curriculum.models import SubjectModel, CurriculumModel, SubjectScheduleModel
from exam.models import ExamModel
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def student (request):
    if request.method == 'POST':
        details = GlobalSession.sessions(request)
        student = StudentModel.objects.filter(student_id=request.session.get('userid')).first()
        schedules = FacultyModel.objects.filter(section_code=student.section_code)
        subjects = SubjectScheduleModel.objects.filter(section=student.section_code)

        subject_dict = serializers.serialize('python', subjects)
        return JsonResponse({ 'subjects': subject_dict })
    else:

        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            student = StudentModel.objects.filter(student_id=request.session.get('userid')).first()
            schedules = FacultyModel.objects.filter(section_code=student.section_code)
            subjects = SubjectScheduleModel.objects.filter(section=student.section_code)
            
            schedule_details = []
            
            # if student.status == 'regular':
            #     schedules = FacultyModel.objects.filter(section_code=student.section_code)
            #     for schedule in schedules:
            #         subject = SubjectModel.objects.filter(subject_code=schedule.subject_code).first()
            #         curriculum = CurriculumModel.objects.filter(subject_code__subject_code=schedule.subject_code).first()
                    
            #         schedule_details.append({
            #             'subject_code': schedule.subject_code,
            #             'subject_name': subject.subject_description,
            #             'units': curriculum.units,
            #             'room': schedule.room,
            #             'day': schedule.days,
            #             'time_in': schedule.time_in,
            #             'time_out': schedule.time_out,
            #         })
            
            # else:
                # schedules = StudentScheduleModel.objects.filter(student_id=request.session.get('userid'))
                
                # for schedule in schedules:
                #     faculty = FacultyModel.objects.filter(id=schedule.faculty_schedule_id).first()
                #     subject = SubjectModel.objects.filter(subject_code=faculty.subject_code).first()
                #     curriculum = CurriculumModel.objects.filter(subject_code__subject_code=faculty.subject_code).first()
                #     schedule_details.append({
                #         'subject_code': faculty.subject_code,
                #         'subject_name': subject.subject_description,
                #         'units': curriculum.units,
                #         'room': faculty.room,
                #         'day': faculty.days,
                #         'time_in': faculty.time_in,
                #         'time_out': faculty.time_out,
                #     })
                
            
            return render(request, 'pages/student.html', {'request': request, 'details': details, 'subjects': subjects})
        else:
            return redirect('/')
    
def student_calendar_details (request):
    if request.method == 'POST':
        student = StudentModel.objects.filter(student_id=request.session.get('userid')).first()
        schedules = FacultyModel.objects.filter(section_code=student.section_code)
        
        schedule_details = []
        
        if student.status == 'regular':
            schedules = FacultyModel.objects.filter(section_code=student.section_code)
            for schedule in schedules:
                subject = SubjectModel.objects.filter(subject_code=schedule.subject_code).first()
                curriculum = CurriculumModel.objects.filter(subject_code__subject_code=schedule.subject_code).first()
                
                schedule_details.append({
                    'subject_code': schedule.subject_code,
                    'subject_name': subject.subject_description,
                    'units': curriculum.units,
                    'room': schedule.room,
                    'day': schedule.days,
                    'time_in': schedule.time_in,
                    'time_out': schedule.time_out,
                })
        
        else:
            schedules = StudentScheduleModel.objects.filter(student_id=request.session.get('userid'))
            
            for schedule in schedules:
                faculty = FacultyModel.objects.filter(id=schedule.faculty_schedule_id).first()
                subject = SubjectModel.objects.filter(subject_code=faculty.subject_code).first()
                curriculum = CurriculumModel.objects.filter(subject_code__subject_code=faculty.subject_code).first()
                schedule_details.append({
                    'subject_code': faculty.subject_code,
                    'subject_name': subject.subject_description,
                    'units': curriculum.units,
                    'room': faculty.room,
                    'day': faculty.days,
                    'time_in': faculty.time_in,
                    'time_out': faculty.time_out,
                })
        
        return JsonResponse(schedule_details, safe=False)