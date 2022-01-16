from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import *
from .models import *

# Create your views here.

def login(request):
    return render(request, 'login.html')
    
def main(request):
    return render(request, 'main.html')

def domain(request):
    if request.method == 'GET':
         form = DomainForm()
    else:
        form = DomainForm(request.POST)
        if form.is_valid():
            form.save()
    dom_list = tb1_master_domain.objects.all()
    return render(request, 'domain.html', {'form':form, 'domain_list':dom_list })

       
def deletedom(request, id):
    dom_obj = tb1_master_domain.objects.get(id=id)
    dom_obj.delete()
    return redirect("/adm/domain")    
    
   
def document(request):
    return render(request, 'document.html')

def url(request):
    if request.method == 'GET':
         form = URLform()
    else:
        form = URLform(request.POST)
        if form.is_valid():
            form.save()
        
    
    url_list = tb2_Url_details_table.objects.all()
    return render(request, 'url.html', {'form':form, 'urls_list':url_list})
    

def deleteurl(request, id):
    url_obj = tb2_Url_details_table.objects.get(id=id)
    url_obj.delete()
    return redirect("/adm/url")    
    
   

def test(request):
    return render(request, 'test.html')  # remmove this path later (for testing purpose only)




