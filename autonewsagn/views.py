from django.http import *
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db import models
from adm_interface.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from gtts import gTTS
import os

language = 'en'

def main(request):
    return render(request, 'index.html')


def sports(request):

    catg_list = Category.objects.filter(name='Sports')
    for x in catg_list:
        catg_id = x.id
    url_list = DomainUrl.objects.filter(category = catg_id)
    url_id = []
    for x in url_list:
        url_id.append(x.id)
    art_list = []
    for y in url_id:
        art_list.append(Article.objects.filter(url = y))
    art_id = []
    for x in art_list:
        for y in x:
            art_id.append(y.id)

    un_data= []
    for x in art_id:
        un_data.append(UnprocesssedScrapeData.objects.filter(article = x))
    un_data_id = []
    for x in un_data:
        for y in x:
            un_data_id.append(y.id)

    prsd_data = []
    for x in un_data_id:
        prsd_data.append(ProcesssedScrapeData.objects.filter(article = x))


    sprt_list = prsd_data
    lst = []
    for x in sprt_list:
        for news in x:
            lst.append(news.processed_news_description)
    s_lst = ''.join(lst)

    output = gTTS(text = s_lst, lang = language, slow = False)
    #output.save("opt_sprt.mp3")

    return render(request, 'sports.html', {'sprt_list':sprt_list, 'output':output})


def tech(request):
    #tech_list = ProcesssedScrapeData.objects.filter(article = UnprocesssedScrapeData.objects.filter(article = Article.objects.filter(url = DomainUrl.objects.filter(category = Category.objects.filter(name='Technology')))))
    #The above statement is decomposed into several sub-statements and then the final news is obtained out of it. (decomposed because we needed only the ids of the objects instead oof the whole object)

    catg_list = Category.objects.filter(name='Technology')
    for x in catg_list:
        catg_id = x.id
    url_list = DomainUrl.objects.filter(category = catg_id)
    url_id = []
    for x in url_list:
        url_id.append(x.id)
    art_list = []
    for y in url_id:
        art_list.append(Article.objects.filter(url = y))
    art_id = []
    for x in art_list:
        for y in x:
            art_id.append(y.id)

    un_data= []
    for x in art_id:
        un_data.append(UnprocesssedScrapeData.objects.filter(article = x))
    un_data_id = []
    for x in un_data:
        for y in x:
            un_data_id.append(y.id)

    prsd_data = []
    for x in un_data_id:
        prsd_data.append(ProcesssedScrapeData.objects.filter(article = x))


    tech_list = prsd_data
    return render(request, 'tech.html', {'tech_list':tech_list})


def entertm(request):
    catg_list = Category.objects.filter(name='Entertainment')
    for x in catg_list:
        catg_id = x.id
    url_list = DomainUrl.objects.filter(category = catg_id)
    url_id = []
    for x in url_list:
        url_id.append(x.id)
    art_list = []
    for y in url_id:
        art_list.append(Article.objects.filter(url = y))
    art_id = []
    for x in art_list:
        for y in x:
            art_id.append(y.id)

    un_data= []
    for x in art_id:
        un_data.append(UnprocesssedScrapeData.objects.filter(article = x))
    un_data_id = []
    for x in un_data:
        for y in x:
            un_data_id.append(y.id)

    prsd_data = []
    for x in un_data_id:
        prsd_data.append(ProcesssedScrapeData.objects.filter(article = x))


    entm_list = prsd_data
    return render(request, 'entertm.html', {'entm_list':entm_list})

    
