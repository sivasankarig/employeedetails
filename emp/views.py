# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http.response import HttpResponseRedirect

from .models import Employee

from .forms import UploadFileForm
from django.utils import timezone
from django.core.files.uploadedfile import UploadedFile

import csv
import io

# Create your views here.

def index(request):
    latest_emp_list = Employee.objects.order_by('id')[:20]
    context = {'latest_emp_list': latest_emp_list}
    return render(request, 'emp/index.html', context)

def insertemp(line):
    name,email=line.split(',')
    try:
        ec=Employee.objects.filter(emp_name=name).count()
        if ec==0:
            emp=Employee(emp_name=name,emp_email=email,pub_date=timezone.now())
            emp.save()
            return True
        
        return False
    except Question.DoesNotExist:
        return False
   



def overwrite(request):
     emplist = request.POST.getlist('overwrite')
     lsize=len(emplist) 
     for line in emplist:
        name,email=line.split(',')
        ec=Employee.objects.filter(emp_name=name).update(emp_email=email)
     return HttpResponse(" %s entries has been successfully overwritten" % lsize)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            ufile=UploadedFile(request.FILES['file'])
            #create a list with alreaduy exist
            econtent=[]
            for line in ufile.readlines():
                if not insertemp(line):
                    econtent.append(line)
            if len(econtent) >0:
               return render(request, 'emp/override.html', {'list': econtent})   
            return HttpResponseRedirect('/emp/success/')
    else:
        form = UploadFileForm()
    return render(request, 'emp/upload.html', {'form': form})

def success(request):
    return HttpResponse("File uploaded successfully")


def add(request):
    return render(request, 'emp/add.html')


def upload(request):
    filename=request.FILES['file']
    paramFile = filename.read()
    for line in paramFile:
        print line
    return render(request, 'emp/detail.html',{'file': filename})


def detail(request, emp_id):
    return HttpResponse("You're looking at question %s." % emp_id)

def results(request, emp_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % emp_id)

def vote(request, emp_id):
    return HttpResponse("You're voting on question %s." % emp_id)

