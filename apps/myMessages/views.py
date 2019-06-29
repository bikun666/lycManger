from django.shortcuts import render
from apps.myMessages.models import Message


def turnToMessageboard(request):
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


def leaveMessage(request):
    if request.method == "POST":
    #     Message.name = request.POST.get('name')
    #     Message.message = request.POST.get('message')
    #     Message.save()
        p = Message(name=request.POST.get('name'), message=request.POST.get('message'))
        p.save()
    return turnToMessageboard(request)