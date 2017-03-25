from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student,Students,Gain,Rank,Invoice,User
from django.db.models import Q
from datetime import date
from django.core.urlresolvers import reverse

# Create your views here.

def hello(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "hello.html", ctx)
    #return render(request, 'hello.html', context)

def profile(request,stu_id):
    stu = get_object_or_404(Students, pk=stu_id)
    return render(request, "profile.html", {'stu': stu})

def edit_profile(request):
    return render(request, "edit.html")

def signup(request):
    ctx={}
    if request.POST:
        # get input value
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        birth_y = int(request.POST['birthday_y'])
        birth_m = int(request.POST['birthday_m'])
        birth_d = int(request.POST['birthday_d'])
        joindate_y = int(request.POST['joindate_y'])
        joindate_m = int(request.POST['joindate_m'])
        joindate_d = int(request.POST['joindate_d'])
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']

        # insert input to database
        stu = Students(stu_fname=firstname, stu_lname=lastname, stu_birth_date=date(birth_y, birth_m, birth_d),
                       stu_join_date=date(joindate_y, joindate_m, joindate_d), stu_phone=phone, stu_email=email,
                       stu_address=address)
        stu.save()
        print(stu.stu_id)
        user = User(username=username,password=password,stu_id=stu)
        user.save()

        # return message
        ctx['rlt']="sign up successfully"
    return render(request, 'signup.html',ctx)


def login(request):
    message = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        #usr = Students.objects.filter(user__password=password,user__username=username)
        usr = User.objects.filter(username=username,password=password)

        if len(usr) == 1:
            stu_id = usr.values()[0]['stu_id_id']
            #print(stu_id)
            #message['id']=stu_id
            return HttpResponseRedirect(reverse('profile',args=(stu_id,)))
        else:
            message['error_message']="incorrect username or password"
            #return render(request, 'login.html',{'error_message':"username or password is incorrect"})

    return render(request, 'login.html', message)


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

    #result_list={}
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