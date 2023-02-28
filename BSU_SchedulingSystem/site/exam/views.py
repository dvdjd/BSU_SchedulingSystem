from django.shortcuts import render, redirect
from global_session import GlobalSession
from curriculum.models import AcademicProgramModel

# Create your views here.
def exam (request):
    if 'username' in request.session and request.session['username'] is not None:
        details = GlobalSession.sessions(request)
        program_codes = AcademicProgramModel.objects.all()
        return render(request, 'pages/exam.html', {'details': details, 'program_codes': program_codes })
    else:
        return redirect('/')