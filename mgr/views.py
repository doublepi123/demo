from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from common.models import Student


def liststudent(request):
    qs = Student.objects.values()

    retStr = ''
    for student in qs:
        for name, value in student.items():
            retStr += f'{name} : {value} | '

        retStr += '<br>'
    return HttpResponse(retStr)