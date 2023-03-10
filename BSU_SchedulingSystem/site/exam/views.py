from django.shortcuts import render, redirect
from global_session import GlobalSession
from curriculum.models import AcademicProgramModel, SectionModel, SubjectModel, CourseModel
from .models import ExamModel

# Create your views here.
def exam (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        program_codes = AcademicProgramModel.objects.all()
        sections = SectionModel.objects.all()
        exams = ExamModel.objects.all()
        
        exam_schedules = []
        
        for exam in exams:
            subject = SubjectModel.objects.filter(subject_code=exam.subject_code).first()
            course = CourseModel.objects.filter(course_code=subject.course_code).first()
            section = SectionModel.objects.filter(section_code=subject.section_code).first()
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
                'program_code': subject.program_code,
                'course': course.course_name,
                'section': subject.section_code,
                'level': level,
                'subject_code': subject.subject_code,
                'subject_description': subject.subject_description,
                'schedule': exam.days + ' ' + exam.time_in.strftime('%I:%M %p') + '-' + exam.time_out.strftime('%I:%M %p')
            })
        return render(request, 'pages/exam.html', {'request': request, 'details': details, 'program_codes': program_codes, 'sections': sections, 'exam_schedules': exam_schedules })
    else:
        return redirect('/')