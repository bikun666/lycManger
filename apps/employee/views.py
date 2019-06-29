from django.http import FileResponse
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


def upload_file(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("no files for upload!")
        else:
            # 打开特定的文件进行二进制的写操作;
            with open("./static/img/%s" % File.name, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("upload over!")
    else:
        return render(request, '../templates/upload.html')


def my_download(request):
    if request.is_ajax():
        path = 'xls/xlsx_file.xlsx'
        # file=open(path,'rb')
        # response =FileResponse(file)
        # response['Content-Type']='application/octet-stream'
        # response['Content-Disposition']='attachment;filename="xlsx_file.xlsx"'
        # return response
        return HttpResponse(json.dumps(path))
    else:
        return render(request, '../templates/my_download.html')


