from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm


def CreateViewSignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:login')
    else:
        form = SignUpForm()
        
    context = {'form': form}
    return render(request, 'homepage/signup.html', context)

