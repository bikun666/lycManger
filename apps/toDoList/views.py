from django.shortcuts import render



def addTodo(request):
    from django.core import serializers
    query = serializers.serialize("json", Message.objects.all())
    users = Message.objects.all()
    # request.session['query'] = query
    print(query)

    # username = []
    # for i in users:
    #     username.append(i.name)
    return render(request, '../templates/message.html', {'username': users})
    # return render(request, '../templates/message.html', {'username': json.dumps(username)})
    # return render(request, '../templates/message.html')


def searchTodo(request):
    if request.method == "POST":
    #     Message.name = request.POST.get('name')
    #     Message.message = request.POST.get('message')
    #     Message.save()
        p = Message(name=request.POST.get('name'), message=request.POST.get('message'))
        p.save()
    return turnToMessageboard(request)


def delTodo(request):
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
