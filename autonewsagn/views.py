from django.http import *
from django.shortcuts import render, HttpResponseRedirect, redirect

def main(request):
    return render(request, 'index.html')

def sports(request):
    return render(request, 'sports.html')

def tech(request):
    return render(request, 'tech.html')

def entertm(request):
    return render(request, 'entertm.html')
   