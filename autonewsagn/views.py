from django.http import *
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db import models
from adm_interface.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sports.html')
        else:
            messages.info(request, "Username OR Password is incorrect")
            return render(request,'login.html', {})


def main(request):
    return render(request, 'index.html')


def sports(request):
    return render(request, 'sports.html')


def tech(request):
    tech_list = ProcesssedScrapeData.objects.filter()
    return render(request, 'tech.html')


def entertm(request):
    return render(request, 'entertm.html')


def reporter_video(request):
    return render(request, 'reporter_video.mp4')
