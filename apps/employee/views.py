from django.shortcuts import render,HttpResponse,redirect,reverse,HttpResponseRedirect
from apps.employee.models import Employee
import json


def show(request):
    return render(request, '../templates/login.html')


def login(request):
    return render(request, '../templates/login.html')


def ajax(request):
    meg = {}
    if request.is_ajax():
        employeeNo = request.POST.get('employeeNo')
        password = request.POST.get('password')
        try:
            query = Employee.objects.get(employeeNo=employeeNo, password=password)
        except:
            meg['meg'] = 'ERROR'
        else:
            request.session['name'] = query.name
            request.session['authority'] = query.authority
        return HttpResponse(json.dumps(meg))
    return render(request, '../templates/login.html')


def goToMenu(request):
    return render(request, '../templates/goToMenu.html')



