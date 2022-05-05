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
 

def updateurl(request,id):
    if request.method == 'GET':
        upd_url = DomainUrl.objects.get(pk=id)
        form = URLform(instance=upd_url)
    else:
         upd_url = DomainUrl.objects.get(pk=id)
         form = URLform(request.POST, instance=upd_url)
         if form.is_valid():
             form.save()
         return redirect("/adm/url") 

    url_list = DomainUrl.objects.all()
    return render(request, 'updateurl.html', {'form':form, 'urls_list':url_list})


def deleteurl(request, id):
    url_obj = DomainUrl.objects.get(id=id)
    url_obj.delete()
    return redirect("/adm/url")    

def config(request, id):
     url_obj = DomainUrl.objects.get(id=id)
     txtform = TextConfrForm()
     imgform = ImgConfrForm()
     dateform = DateConfrForm()
     headlineform = HeadlineConfrForm()
     urlform = URLConfrForm()

     if request.method == 'POST' and 'add_config' in request.POST:
        txtform = TextConfrForm(request.POST)
        if txtform.is_valid():
            url_id = url_obj
            tag_nm = txtform.cleaned_data['tag_name']
            att_nm = txtform.cleaned_data['attribute_name']
            scrp_type = txtform.cleaned_data['scrape_type']
            text_conf = ArticleTextConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()


     if request.method == 'POST' and 'img_config' in request.POST:
        imgform = ImgConfrForm(request.POST)
        if imgform.is_valid():
            url_id = url_obj
            tag_nm = imgform.cleaned_data['tag_name']
            att_nm = imgform.cleaned_data['attribute_name']
            scrp_type = imgform.cleaned_data['scrape_type']
            text_conf = ArticleImgConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()


     if request.method == 'POST' and 'date_config' in request.POST:
        dateform = DateConfrForm(request.POST)
        if dateform.is_valid():
            url_id = url_obj
            tag_nm = dateform.cleaned_data['tag_name']
            att_nm = dateform.cleaned_data['attribute_name']
            scrp_type = dateform.cleaned_data['scrape_type']
            text_conf = ArticlePublishDateConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()


     if request.method == 'POST' and 'headline_config' in request.POST:
        headlineform = HeadlineConfrForm(request.POST)
        if headlineform.is_valid():
            url_id = url_obj
            pt_tag_nm = headlineform.cleaned_data['parent_tag_name']
            cd_tag_nm = headlineform.cleaned_data['child_tag_name']
            att_nm = headlineform.cleaned_data['attribute_name']
            scrp_type = headlineform.cleaned_data['scrape_type']
            text_conf = ArticleTopicHeadlineConfiguration(domain_url=url_id, parent_tag_name=pt_tag_nm, child_tag_name=cd_tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()

     if request.method == 'POST' and 'url_config' in request.POST:
        urlform = URLConfrForm(request.POST)
        if  urlform.is_valid():
            url_id = url_obj
            tag_nm = urlform.cleaned_data['tag_name']
            att_nm = urlform.cleaned_data['attribute_name']
            scrp_type = urlform.cleaned_data['scrape_type']
            text_conf = ArticleUrlConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()



     config_list = ArticleTextConfiguration.objects.all()
     return render(request, 'config.html', {'txtform': txtform, 'imgform': imgform, 'dateform': dateform, 'headlineform': headlineform, 'urlform': urlform, 'config_list':config_list})
    


def test(request,id):   # remmove this path later (for testing purpose only)
    url_obj = DomainUrl.objects.get(id=id)
    txtform = TextConfrForm()
    imgform = ImgConfrForm()
    dateform = DateConfrForm()
    headlineform = HeadlineConfrForm()
    urlform = URLConfrForm()

    if request.method == 'POST' and 'add_config' in request.POST:
        txtform = TextConfrForm(request.POST)
        if txtform.is_valid():
            url_id = url_obj
            tag_nm = txtform.cleaned_data['tag_name']
            att_nm = txtform.cleaned_data['attribute_name']
            scrp_type = txtform.cleaned_data['scrape_type']
            text_conf = ArticleTextConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()


    if request.method == 'POST' and 'img_config' in request.POST:
        imgform = ImgConfrForm(request.POST)
        if imgform.is_valid():
            url_id = url_obj
            tag_nm = imgform.cleaned_data['tag_name']
            att_nm = imgform.cleaned_data['attribute_name']
            scrp_type = imgform.cleaned_data['scrape_type']
            text_conf = ArticleImgConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()


    if request.method == 'POST' and 'date_config' in request.POST:
        dateform = DateConfrForm(request.POST)
        if dateform.is_valid():
            url_id = url_obj
            tag_nm = dateform.cleaned_data['tag_name']
            att_nm = dateform.cleaned_data['attribute_name']
            scrp_type = dateform.cleaned_data['scrape_type']
            text_conf = ArticlePublishDateConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()


    if request.method == 'POST' and 'headline_config' in request.POST:
        headlineform = HeadlineConfrForm(request.POST)
        if headlineform.is_valid():
            url_id = url_obj
            pt_tag_nm = headlineform.cleaned_data['parent_tag_name']
            cd_tag_nm = headlineform.cleaned_data['child_tag_name']
            att_nm = headlineform.cleaned_data['attribute_name']
            scrp_type = headlineform.cleaned_data['scrape_type']
            text_conf = ArticleTopicHeadlineConfiguration(domain_url=url_id, parent_tag_name=pt_tag_nm, child_tag_name=cd_tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()

    if request.method == 'POST' and 'url_config' in request.POST:
        urlform = URLConfrForm(request.POST)
        if  urlform.is_valid():
            url_id = url_obj
            tag_nm = urlform.cleaned_data['tag_name']
            att_nm = urlform.cleaned_data['attribute_name']
            scrp_type = urlform.cleaned_data['scrape_type']
            text_conf = ArticleUrlConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()



    config_list = ArticleTextConfiguration.objects.all()
    return render(request, 'test.html', {'txtform': txtform, 'imgform': imgform, 'dateform': dateform, 'headlineform': headlineform, 'urlform': urlform, 'config_list':config_list})
    




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




