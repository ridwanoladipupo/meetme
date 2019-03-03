from django.shortcuts import render
from django.http import HttpResponse

from signup.models import Cridentials

def CreateViewMain(request):
    
    try:
        forms = Cridentials.objects.all()
    except MyUser.DoesNotExist:
        forms = None

    return render(request, 'homepage/main.html', {'forms': forms})
  