
from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from . import constent
from.models import *
from django.core import serializers
import ast
import json

@csrf_exempt
def Login(request):
    return render(request,'login_administrator.html')

@csrf_exempt
def Homepage(request):
    if request.method == 'POST':
        First_Name = request.POST.get('your_firstname')
        Last_Name = request.POST.get('your_lastname')
        Date_Birth = request.POST.get('date_birth')
        Phone = request.POST.get('phone_no')
        Email = request.POST.get('emailid')
        Location = request.POST.get('your_location')
        Organisation = request.POST.get('your_organisation')
        Experience = request.POST.get('your_experience')
        Re_experience = request.POST.get('your_relevant_experience')
        Designation = request.POST.get('your_designation')
        Skill = request.POST.get('your_skill')
        Nationality = request.POST.get('nationality')
        Myfile = request.POST.get('myfile')
        if First_Name and Last_Name and Date_Birth and Phone and Email and Location and Organisation and Experience and Re_experience and  Designation and Skill and Nationality:
            if Myfile:
                Action = 1
                Actiontype = 'submit'
                data = Employeedetails(fname=First_Name, lname=Last_Name, phone=Phone, d_b=Date_Birth, email=Email,
                                       location=Location, organisation=Organisation, experience=Experience,
                                       re_experience=Re_experience, designation=Designation, skills=Skill, nationality=Nationality,
                                       action=Action, action_type=Actiontype,  docfile=Myfile)
                data.save()
                return render(request,'homepage.html')
            return render(request, 'homepage.html', {'massage_resume': 'Please upload resume','fname':First_Name, 'lname':Last_Name,
                                                     'd_b':Date_Birth, 'phone':Phone, 'email':Email, 'location':Location, 'org':Organisation,
                                                     'exp':Experience, 're_exp':Re_experience, 'desig':Designation, 'skills':Skill, 'nationality':Nationality})
        else:
            return render(request, 'homepage.html', {'massage' :'Please fill in the all fields'})

    else:
        return render(request,'homepage.html', {'massage' :''})


def View_Profile(req):
    if req.method == 'GET':
        User_name = req.GET.get('username')
        Accept_Status = req.GET.get('accept')
        Reject_Status = req.GET.get('reject')
        if Accept_Status is not None:
            Name = Accept_Status
            Value =2
            Type_action ='accept'
            data =Employeedetails.objects.filter(fname=Name).update(action=str(Value), action_type=Type_action)
            orm_cou = Employeedetails.objects.all()
            data = serializers.serialize('json', orm_cou)
            j = json.loads(data)
            emp_data = []
            for i in j:
                if i['fields']['action'] == 1:
                    fname = i['fields']['fname']
                    lname = i['fields']['lname']
                    emp_data.append({'fname': fname, 'lname': lname})
            context = {'data': emp_data}
            return render(req, 'index.html', context)

        elif Reject_Status is not None:
            Name = Reject_Status
            Value = 3
            Type_action = 'reject'
            data =Employeedetails.objects.filter(fname=Name).update(action=str(Value), action_type=Type_action)
            orm_cou = Employeedetails.objects.all()
            data = serializers.serialize('json', orm_cou)
            j = json.loads(data)
            emp_data = []
            for i in j:
                if i['fields']['action'] == 1:
                    fname = i['fields']['fname']
                    lname = i['fields']['lname']
                    emp_data.append({'fname': fname, 'lname': lname})
            context = {'data': emp_data}
            return render(req, 'index.html', context)

        Name =User_name
        x=Employeedetails.objects.filter(fname=Name)
        data = serializers.serialize('json', x)
        j = json.loads(data)
        context = {'data': j}
        return render(req, 'view_profile.html',context)




def Index(request):

    if request.method == 'POST':
        User_name = request.POST.get('username')
        Pass_word = request.POST.get('password')
        if User_name and Pass_word:
            if User_name == constent.Username and Pass_word == constent.Password:
                orm_cou = Employeedetails.objects.all()
                data = serializers.serialize('json', orm_cou)
                j = json.loads(data)
                emp_data =[]
                for i in j:
                    if i['fields']['action']==1:
                        fname =i['fields']['fname']
                        lname =i['fields']['lname']
                        emp_data.append({'fname':fname, 'lname':lname})
                context = {'data': emp_data}
                return render(request,'index.html', context)
            else:
                return render(request, 'login_administrator.html', {'massage' :'Invalid Username and Password'})
        else:
            return render(request, 'login_administrator.html', {'massage': 'Please enter Username and Password'})
    else:
        orm_cou = Employeedetails.objects.all()
        data = serializers.serialize('json', orm_cou)
        j = json.loads(data)
        emp_data = []
        for i in j:
            if i['fields']['action'] == 1:
                fname = i['fields']['fname']
                lname = i['fields']['lname']
                emp_data.append({'fname': fname, 'lname': lname})
        context = {'data': emp_data}
        return render(request, 'index.html', context)