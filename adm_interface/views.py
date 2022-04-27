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
    dom_list = Category.objects.all()
    return render(request, 'domain.html', {'form':form, 'domain_list':dom_list })

       
def deletedom(request, id):
    dom_obj = Category.objects.get(id=id)
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
    

    url_list = DomainUrl.objects.all()
    return render(request, 'url.html', {'form':form, 'urls_list':url_list})
    

def deleteurl(request, id):
    url_obj = DomainUrl.objects.get(id=id)
    url_obj.delete()
    return redirect("/adm/url")    

def config(request, id):
    url_obj = DomainUrl.objects.get(id=id)
    if request.method == 'POST':
        form = TextConfiguraton(request.POST)
        if form.is_valid():
             url_id = url_obj
             tag_nm = form.cleaned_data['tag_name']
             scrp_type = form.cleaned_data['scrape_type']
             att_nm = form.cleaned_data['attribute_name']
             text_conf = ArticleTextConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
             text_conf.save()
    else:
        form = TextConfiguraton()
    config_list = ArticleTextConfiguration.objects.all()
    return render(request,'config.html',  {'form':form, 'config_list':config_list})


def test(request):
    return render(request, 'test.html')  # remmove this path later (for testing purpose only)

def check_config(request):
    return render(request, 'check_config.html')

def img_config(request):
    return render(request, 'img_config.html')

def text_config(request):
    return render(request, 'text_config.html')

def headline_config(request):
    return render(request, 'headline_config.html')

def time_config(request):
    return render(request, 'time_config.html')




