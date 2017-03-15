from django.shortcuts import render,render_to_response
from .models import Student,Students,Gain,Rank,Invoice
from django.db.models import Q

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

    # student_list = Student.objects.all().order_by('stu_join_date')
    # for k in request.GET:
    #     message = request.GET[k]
    #     #print(message)
    #     if message is not '':
    #         if k =='stu_fname':
    #             student_list = student_list.filter(stu_fname=message)
    #         elif k=='stu_join_date':
    #             student_list = student_list.filter(stu_join_date__gt=message)
    # context ={
    #     'student_list': student_list
    # }

    result_list={}
    active_students = Students.objects.all()
    student_list = Students.objects.all()
    invoice_list = Invoice.objects.all()
    belt_color =[]
    condition = []
    #object_list = Students.objects.filter(gain__rank_id__rank_belt_color='Yellow')
    # print(object_list)
    # for item in object_list:
    #     print(item.stu_fname,item.stu_join_date)
    for k in request.GET:
        message = request.GET[k]
        if message is not '':
            if k == 'stu_fname':
                student_list = student_list.filter(stu_fname=message)
                condition.append('Student First Name: '+message)
            elif k =='stu_lname':
                student_list = student_list.filter(stu_lname=message)
                condition.append('Student Last Name: ' + message)
            elif k == 'join_date1':
                student_list = student_list.filter(stu_join_date__gte=message)
            elif k == 'join_date2':
                student_list = student_list.filter(stu_join_date__lte=message)
            elif k == 'belt_color':
                belt_color.append(message)
            elif k == 'inv_date1':
                invoice_list = invoice_list.filter(inv_date__gte=message)
            elif k== 'inv_date2':
                invoice_list = invoice_list.filter(inv_date__lte=message)
    if len(belt_color)==1:
        student_list = student_list.filter(gain__rank_id__rank_belt_color=belt_color[0])
    elif len(belt_color)==2:
        student_list = student_list.filter(Q(gain__rank_id__rank_belt_color=belt_color[0]) |
                                           Q(gain__rank_id__rank_belt_color=belt_color[1]))
    print(student_list.values())
    print(invoice_list.values())

    context = {
        'student_list':student_list,
        'active_students': active_students,
        'invoice_list': invoice_list
    }
    return render(request,'report.html',context)