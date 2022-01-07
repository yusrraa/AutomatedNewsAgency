from django.shortcuts import render, HttpResponse, redirect
from .forms import DomainForm
from .models import tb1_master_domain

# Create your views here.

def login(request):
    return render(request, 'login.html')
    
def main(request):
    return render(request, 'main.html')

def domain(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            form.save()
        #dom_list = {'domain_list':tb1_master_domain.objects.all()}
        return redirect('adm_interface/domain.html') 
        
    else:
        form = DomainForm()
        return render(request, 'domain.html', {'form':form})


   
def document(request):
    return render(request, 'document.html')

def url(request):
    return render(request, 'url.html')

def test(request):
    return render(request, 'test.html')  # remmove this path later (for testing purpose only)




