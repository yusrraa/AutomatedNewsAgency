from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html')
    
def main(request):
    return render(request, 'main.html')
