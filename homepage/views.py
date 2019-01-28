from django.shortcuts import render
from django.http import HttpResponse


def CreateViewHome(request):
    return render(request, 'homepage/index.html')
