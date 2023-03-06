from django.shortcuts import render, redirect
from django.core import serializers
from global_session import GlobalSession
from loginuser.models import LoginUser
from curriculum.models import AcademicProgramModel, SubjectModel
from pages.models import FacultyModel
from room.models import RoomModel
from django.http import JsonResponse

# Create your views here.
def room (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        program_codes = AcademicProgramModel.objects.all().values('id', 'program_code')
        rooms = RoomModel.objects.all().values('id', 'room')
        user = LoginUser.objects
        subject = SubjectModel.objects
        faculty = FacultyModel.objects.all().values('instructor_id', 'subject_code', 'room', 'days', 'time_in', 'time_out')
        room = RoomModel.objects
        schedules = []
        for fac in faculty:
            instructor = user.filter(userid=fac['instructor_id']).first()
            subj = subject.filter(id=fac['subject_code']).first()
            classroom = room.filter(id=fac['room']).first()
            schedules.append({
                'instructor': instructor.firstname + ' ' + instructor.lastname,
                'subject': subj.subject_code,
                'program_code': subj.program_code,
                'days': fac['days'],
                'time_in': fac['time_in'],
                'time_out': fac['time_out'],
                'room': classroom.room,
            })
        print(schedules)
        return render(request, 'pages/room.html', {'request': request, 'details': details, 'program_codes': program_codes, 'rooms': rooms, 'schedules': schedules })
    else:
        return redirect('/')
    
def search_room (request): 
    if request.method == 'POST':
        room = request.POST.get('room')
        program_code = request.POST.get('program_code')
        print(room, program_code)
        result = FacultyModel.objects.select_related('subject_code').filter(room=room)
        data = serializers.serialize('json', result)

        return JsonResponse(data, safe=False)
    else:
        pass