from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import *
from .models import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pymysql


# Create your views here.


def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'main.html')
        else:
            messages.info(request, "Username OR Password is incorrect")
            return render(request,'login.html', {})

    return render(request, 'login.html')

@login_required(login_url = '')
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

    doc_list = ProcesssedScrapeData.objects.all() 
    return render(request, 'document.html', {'doc_list':doc_list})

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

def disableurl(request,id):
    # database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                 database="automated_news_broadcast")
    cursor = connection.cursor()
    # Disable the URl
    #extracted_id = DomainUrl.objects.get(id=id)
    disable_url = cursor.execute("Update domain_url set is_active=0 where id=id")
    connection.close()
    return redirect("/adm/url")
 


def config(request, id):
     url_obj = DomainUrl.objects.get(id=id)
     txtform = TextConfrForm()
     imgform = ImgConfrForm()
     dateform = DateConfrForm()
     headlineform = HeadlineConfrForm()
     urlform = URLConfrForm()
     x = ""

     if request.method == 'POST' and 'add_config' in request.POST:
        txtform = TextConfrForm(request.POST)
        if txtform.is_valid():
            url_id = url_obj
            tag_nm = txtform.cleaned_data['tag_name']
            att_nm = txtform.cleaned_data['attribute_name']
            scrp_type = txtform.cleaned_data['scrape_type']
            text_conf = ArticleTextConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()

     if request.method == 'POST' and 'check_config_text' in request.POST:
        txtform = TextConfrForm(request.POST)
        if txtform.is_valid():
            url = url_obj.url
            tag_nm = txtform.cleaned_data['tag_name']
            att_nm = txtform.cleaned_data['attribute_name']
            scrp_type = txtform.cleaned_data['scrape_type']

            options = Options()
            options.headless = True
            s = Service("F:/Program Files (x86)/chromedriver.exe")
            driver = webdriver.Chrome(service=s, options=options)
            #print("shit shhit shi",url)
            driver.get(url)
            time.sleep(5)
            doc = BeautifulSoup(driver.page_source, "html.parser")

            remove_tag = ['header', 'script', 'noscript', 'img', 'footer', 'figure', "button", "input","ul"
                "style","sup","hr","br","iframe","label","nav","form","svg", 'meta','fieldset',"li","ins","style"]
            for sel_tag in remove_tag:
                for scr in doc.find_all(sel_tag):
                    scr.decompose()

            if scrp_type == 'Scrape by ID':
                page_text = doc.find_all(tag_nm,id = att_nm)
                for scrp in page_text:
                    content = scrp.contents
                    for grab in content:
                        if str(grab.string) == "None" or str(grab.string) is None or str(grab.string) == "\n":
                            print("nahh")
                            pass
                        else:
                            print(grab.string)
                            x = grab.string

            else:
                page_text = doc.find_all(tag_nm,class_=att_nm)
                for scrp in page_text:
                    content = scrp.contents
                    for grab in content:
                        if str(grab.string) == "None" or str(grab.string) is None or str(grab.string) == "\n":
                            print("nahh2")
                            pass
                        else:
                            print(grab.string)
                            x = grab.string

     if request.method == 'POST' and 'img_config' in request.POST:
        imgform = ImgConfrForm(request.POST)
        if imgform.is_valid():
            url_id = url_obj
            tag_nm = imgform.cleaned_data['tag_name']
            att_nm = imgform.cleaned_data['attribute_name']
            scrp_type = imgform.cleaned_data['scrape_type']
            text_conf = ArticleImgConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()
     
     if request.method == 'POST' and 'check_config_img' in request.POST:
        imgform = ImgConfrForm(request.POST)
        if imgform.is_valid():
            url = url_obj.url
            tag_nm = imgform.cleaned_data['tag_name']
            att_nm = imgform.cleaned_data['attribute_name']
            scrp_type = imgform.cleaned_data['scrape_type']

            options = Options()
            options.headless = True
            s = Service("F:/Program Files (x86)/chromedriver.exe")
            driver = webdriver.Chrome(service=s, options=options)
            driver.get(url)
            time.sleep(5)
            doc = BeautifulSoup(driver.page_source, "html.parser")
            # driver.quit()

            if scrp_type == 'Scrape by ID':
                li = doc.find(tag_nm, {'id': att_nm})
                for descendant in li.descendants:
                    if descendant.name == "img":
                        print(descendant['src'])
                        x = descendant['src']
                        
            else:
                li = doc.find(tag_nm, {'class': att_nm})
                for descendant in li.descendants:
                    if descendant.name == "img":
                        print(descendant['src'])
                        x = descendant['src']
           

     if request.method == 'POST' and 'date_config' in request.POST:
        dateform = DateConfrForm(request.POST)
        if dateform.is_valid():
            url_id = url_obj
            tag_nm = dateform.cleaned_data['tag_name']
            att_nm = dateform.cleaned_data['attribute_name']
            scrp_type = dateform.cleaned_data['scrape_type']
            text_conf = ArticlePublishDateConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()
            
     if request.method == 'POST' and 'check_config_date' in request.POST:
        dateform = DateConfrForm(request.POST)
        if dateform.is_valid():
            url = url_obj.url
            tag_nm = dateform.cleaned_data['tag_name']
            att_nm = dateform.cleaned_data['attribute_name']
            scrp_type = dateform.cleaned_data['scrape_type']

            options = Options()
            options.headless = True
            s = Service("F:/Program Files (x86)/chromedriver.exe")
            driver = webdriver.Chrome(service=s, options=options)
            driver.get(url)
            time.sleep(5)
            doc = BeautifulSoup(driver.page_source, "html.parser")

            if scrp_type == 'Scrape by ID':
                time_date_publish = doc.find_all(tag_nm, {'class': att_nm})
                print(time_date_publish[0].text)
            else:
                print("None")




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
     

     if request.method == 'POST' and 'check_config_headline' in request.POST:
        headlineform = HeadlineConfrForm(request.POST)
        if headlineform.is_valid():
            url = url_obj.url
            pt_tag_nm = headlineform.cleaned_data['parent_tag_name']
            cd_tag_nm = headlineform.cleaned_data['child_tag_name']
            att_nm = headlineform.cleaned_data['attribute_name']
            scrp_type = headlineform.cleaned_data['scrape_type']

            options = Options()
            options.headless = True
            s = Service("F:/Program Files (x86)/chromedriver.exe")
            driver = webdriver.Chrome(service=s, options=options)
            driver.get(url)
            time.sleep(5)
            doc = BeautifulSoup(driver.page_source, "html.parser")

            article_headline = ""
            if scrp_type == 'Scrape by ID':
                article_topic_headline = doc.find(pt_tag_nm, {'id': att_nm})
                for item in article_topic_headline.find(cd_tag_nm):
                    if str(item.string) is None or str(item.string) == "None" or str(item.string) == "\n":
                        pass
                    else:
                        article_headline += str(item.string)
                        x = item.string
            else:
                article_topic_headline = doc.find(pt_tag_nm, {'class': att_nm})
                for item in article_topic_headline.find(cd_tag_nm):
                    if str(item.string) is None or str(item.string) == "None" or str(item.string) == "\n":
                       pass
                    else:
                       article_headline += str(item.string)
                       x = item.string


     if request.method == 'POST' and 'url_config' in request.POST:
        urlform = URLConfrForm(request.POST)
        if  urlform.is_valid():
            url_id = url_obj
            tag_nm = urlform.cleaned_data['tag_name']
            att_nm = urlform.cleaned_data['attribute_name']
            scrp_type = urlform.cleaned_data['scrape_type']
            text_conf = ArticleUrlConfiguration(domain_url=url_id, tag_name=tag_nm, scrape_type=scrp_type, attribute_name=att_nm)
            text_conf.save()


     if request.method == 'POST' and 'check_config_url' in request.POST:
        urlform = URLConfrForm(request.POST)
        if urlform.is_valid():
            url = url_obj.url
            tag_nm = urlform.cleaned_data['tag_name']
            att_nm = urlform.cleaned_data['attribute_name']
            scrp_type = urlform.cleaned_data['scrape_type']

            




     config_list = ArticleTextConfiguration.objects.filter(domain_url=url_obj)
     return render(request, 'config.html', {'txtform': txtform, 'imgform': imgform, 'dateform': dateform, 'headlineform': headlineform, 'urlform': urlform, 'config_list':config_list, 'chk_config':x})
    


def test(request):   # remmove this path later (for testing purpose only)
    return render(request, 'test.html')




