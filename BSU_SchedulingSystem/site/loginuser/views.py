from django.shortcuts import render, redirect
from .models import LoginUser
from student.models import StudentModel
from pages.models import FacultyModel
from curriculum.models import CourseModel
from global_session import GlobalSession
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index (request):
    
    error = False
    blank = False
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username != '' and password != '':
            user = LoginUser.objects.filter(username=username, password=password)
            if user:
                request.session['username'] = user[0].username
                request.session['firstname'] = user[0].firstname
                request.session['middlename'] = user[0].middlename
                request.session['lastname'] = user[0].lastname
                request.session['userid'] = user[0].userid
                request.session['usertype'] = user[0].usertype
                return redirect('home')
            else:
                error = True
        else:
            blank = True
            
        return render(request, 'pages/login.html', {'error': error, 'blank': blank})
    else:
        if 'username' in request.session and request.session['username'] is not None:
            return redirect('home')
        else:
            return render(request, 'pages/login.html', {'error': error, 'blank': blank})
        
def add_student (request):
    if request.method == 'POST':
        user = LoginUser(userid=request.POST.get('userid'), username=request.POST.get('username'), password=request.POST.get('password'), firstname=request.POST.get('firstname'), middlename=request.POST.get('middlename'), lastname=request.POST.get('lastname'), usertype='student')
        user.save()
        student = StudentModel(student_id=request.POST.get('userid'), level=request.POST.get('level'), course_code=request.POST.get('course'), program_code=request.POST.get('program'), section_code=request.POST.get('section'), status=request.POST.get('status'))
        student.save()
        return HttpResponse('success')
    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            students = LoginUser.objects.filter(usertype='student')
            courses = CourseModel.objects.all()
            
            student_details = []
            for student in students:
                student_program = StudentModel.objects.filter(student_id=student.userid).first()
                student_details.append({
                    'userid': student.userid,
                    'firstname': student.firstname,
                    'middlename': student.middlename,
                    'lastname': student.lastname,
                    'program_code': student_program.program_code
                })
                
            return render(request, 'pages/add_student.html', { 'details': details, 'students': student_details, 'courses': courses })
        else:
            return redirect('/')
        
def search_status (request):
    if request.method == 'POST': 
        students = StudentModel.objects.filter(status=request.POST.get('status'))
        student_details = []
        for student in students:
            student_program = LoginUser.objects.filter(userid=student.student_id).first()
            student_details.append({
                'userid': student.student_id,
                'firstname': student_program.firstname,
                'middlename': student_program.middlename,
                'lastname': student_program.lastname,
                'program_code': student.program_code
            })
            
        return JsonResponse(student_details, safe=False)
    

def add_instructor (request):
    if request.method == 'POST':
        user = LoginUser(userid=request.POST.get('userid'), username=request.POST.get('username'), password=request.POST.get('password'), firstname=request.POST.get('firstname'), middlename=request.POST.get('middlename'), lastname=request.POST.get('lastname'), usertype='instructor')
        user.save()
        return HttpResponse('success')
    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            
            instructors = LoginUser.objects.filter(usertype='instructor')
            
            instructor_details = []
            for instructor in instructors:
                instructor_program = FacultyModel.objects.filter(instructor_id=instructor.userid).first()
                instructor_details.append({
                    'userid': instructor.userid,
                    'firstname': instructor.firstname,
                    'middlename': instructor.middlename,
                    'lastname': instructor.lastname,
                    # 'program_code': instructor_program.program_code
                })
            return render(request, 'pages/add_instructor.html', { 'details': details, 'instructors': instructor_details })
        else:
            return redirect('/')
    
def change_password (request):
    if request.method == 'POST':
        user = LoginUser.objects.get(userid=request.session.get('userid'))
        user.password = request.POST.get('password')
        user.save()
        return HttpResponse('success')
    else:
        if 'username' in request.session and request.session['username'] is not None:
            details = GlobalSession.sessions(request)
            return render(request, 'pages/change_password.html', { 'details': details })
        else:
            return redirect('/')
    
def delete_user (request):
    if request.method == 'POST':
        user = LoginUser.objects.get(userid=request.POST.get('userid')).delete()
        student = StudentModel.objects.get(student_id=request.POST.get('userid')).delete()
        
        return HttpResponse('deleted')

def logout (request):
    request.session.flush()
    return redirect('/')