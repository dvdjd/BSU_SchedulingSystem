from django.shortcuts import render, redirect
from global_session import GlobalSession
from curriculum.models import AcademicProgramModel
from room.models import RoomModel

# Create your views here.
def room (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        program_codes = AcademicProgramModel.objects.all()
        rooms = RoomModel.objects.all()
        return render(request, 'pages/room.html', {'details': details, 'program_codes': program_codes, 'rooms': rooms })
    else:
        return redirect('/')