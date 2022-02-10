from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    aboutdata = about.objects.all()[0]
    context = {
        'about': aboutdata

    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        infodata = Info(name=name, email=email, message=message)
        infodata.save()
    return render(request, 'index.html', context)



