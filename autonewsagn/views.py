from django.http import *
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db import models
from adm_interface.models import *

def main(request):
    return render(request, 'index.html')

def sports(request):
    return render(request, 'sports.html')

def tech(request):
    tech_list = ProcesssedScrapeData.objects.filter()
    return render(request, 'tech.html')

def entertm(request):
    return render(request, 'entertm.html')
   