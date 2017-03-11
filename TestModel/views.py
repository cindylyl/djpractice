from django.shortcuts import render,render_to_response
from .models import Student

# Create your views here.
def hello(request):
    context = {}
    context['hello'] = 'hello, lovely cindy! '
    return render(request, 'hello.html', context)

def profile(request):
    return render(request, "profile.html")

def edit_profile(request):
    return render(request, "edit.html")

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def report_filter(request):
    return render_to_response('report_filter.html')

def report(request):
    request.encoding = 'utf-8'
    # if 'fname' in request.GET:
    #     message = request.GET['fname'].encode('utf-8')
    #student_list = Student.objects.filter(stu_fname=message).order_by('stu_join_date')
    student_list = Student.objects.all().order_by('stu_join_date')
    for k in request.GET:
        message = request.GET[k].encode('utf-8')
        if k =='stu_fname':
            student_list = student_list.filter(stu_fname=message)
        elif k=='stu_lname':
            student_list = student_list.filter(stu_lname=message)
    context ={
        'student_list': student_list
    }
    return render(request,'report.html',context)