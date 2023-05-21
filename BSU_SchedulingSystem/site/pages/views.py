from django.shortcuts import render, redirect
from global_session import GlobalSession
from .models import FacultyModel
from curriculum.models import SubjectModel, CurriculumModel, SectionModel, SubjectScheduleModel
from loginuser.models import LoginUser
from django.http import JsonResponse
from django.core import serializers

def home (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        return render(request, 'pages/home.html', {'request': request, 'details': details})
    else:
        return redirect('/')
    
def faculty (request):
    if request.method == 'POST':
        details = GlobalSession.sessions(request)
        schedules = FacultyModel.objects.filter(instructor_id=request.session.get('userid'))
        name = request.session.get('firstname') + ' ' + request.session.get('lastname')
        subjects = SubjectScheduleModel.objects.filter(profesor=name)

        subject_dict = serializers.serialize('python', subjects)
        return JsonResponse({ 'subjects': subject_dict })

    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            schedules = FacultyModel.objects.filter(instructor_id=request.session.get('userid'))
            schedule_details = []
            # for schedule in schedules:
            #     subject = SubjectModel.objects.filter(subject_code=schedule.subject_code).first()
            #     curriculum = CurriculumModel.objects.filter(subject_code__subject_code=schedule.subject_code).first()
            #     section = SectionModel.objects.filter(section_code=schedule.section_code).first()
            #     user = LoginUser.objects.filter(userid=schedule.instructor_id).first()
                
            #     if section.level == '1':
            #         level = '1st Year'
            #     elif section.level == '2':
            #         level = '2nd Year'
            #     elif section.level == '3':
            #         level = '3rd Year'
            #     elif section.level == '4':
            #         level = '4th Year'
                    
            #     schedule_details.append({
            #         'subject_code': schedule.subject_code,
            #         'subject_name': subject.subject_description,
            #         'units': curriculum.units,
            #         'section': schedule.section_code,
            #         'room': schedule.room,
            #         'day': schedule.days,
            #         'time_in': schedule.time_in,
            #         'time_out': schedule.time_out,
            #         'level': level,
            #         'first_name': user.firstname,
            #         'middle_name': user.middlename,
            #         'last_name': user.lastname,
            #     })
                
            return render(request, 'pages/faculty.html', {'request': request, 'details': details, 'schedules': schedule_details })
        else:
            return redirect('/')
    
# def faculty_calendar_details (request):
#     if request.method == 'POST':
#         schedules = FacultyModel.objects.filter(instructor_id=request.session.get('userid'))
#         schedule_details = []
#         for schedule in schedules:
#             subject = SubjectModel.objects.filter(subject_code=schedule.subject_code).first()
#             curriculum = CurriculumModel.objects.filter(subject_code__subject_code=schedule.subject_code).first()
#             section = SectionModel.objects.filter(section_code=schedule.section_code).first()
#             user = LoginUser.objects.filter(userid=schedule.instructor_id).first()
            
#             if section.level == '1':
#                 level = '1st Year'
#             elif section.level == '2':
#                 level = '2nd Year'
#             elif section.level == '3':
#                 level = '3rd Year'
#             elif section.level == '4':
#                 level = '4th Year'
                
#             schedule_details.append({
#                 'subject_code': schedule.subject_code,
#                 'subject_name': subject.subject_description,
#                 'units': curriculum.units,
#                 'section': schedule.section_code,
#                 'room': schedule.room,
#                 'day': schedule.days,
#                 'time_in': schedule.time_in,
#                 'time_out': schedule.time_out,
#                 'level': level,
#                 'first_name': user.firstname,
#                 'middle_name': user.middlename,
#                 'last_name': user.lastname,
#             })
            
#         return JsonResponse(schedule_details, safe=False)