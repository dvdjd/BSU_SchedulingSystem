from django.shortcuts import render, redirect
from global_session import GlobalSession
from pages.models import FacultyModel
from student.models import StudentModel, StudentScheduleModel
from curriculum.models import SubjectModel, CurriculumModel
from django.db.models import Q

# Create your views here.
def student (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
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
            
        
        return render(request, 'pages/student.html', {'request': request, 'details': details, 'schedules': schedule_details})
    else:
        return redirect('/')