from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def liststudent(request):
    return HttpResponse('下面是学生列表')
