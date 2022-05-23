from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import re


def news_article_scrapper(url, tag_name, scrape_by, att_name):
    options = webdriver.ChromeOptions()
    options.headless = True
    s = Service("F:/Program Files (x86)/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    # url = input("Enter Url: ")
    driver.get(url)
    # time.sleep(5)
    doc = BeautifulSoup(driver.page_source, "html.parser")
    # tag_name = input("Input Tag Name: ")
    # scrape_by = int(input("Enter \n(1)To Scrape By ID \n(2)To Scrape BY Class: "))
    url_domain_id = re.search('/(.+?)/', url).group(0)
    url_id_extract = "https:" + url_domain_id
    if scrape_by == "id":
        # att_name = input("Input ID Name: ")
        article_url_extract = doc.find_all(tag_name, {'id': att_name})
        for tag in article_url_extract:
            # print(tag)
            for item in tag.find_all('a', attrs={'href': re.compile("^https://")}):
                try:
                    condition_true_url = (re.search(url_id_extract, item.get('href')).group() == url_id_extract)
                    article_url_extract = re.search(url_id_extract, item.get('href')).group()
                    # print(article_url_extract)
                    if (len(item.get('href')) - len(article_url_extract)) > 50:
                        print(item.get('href'))
                    else:
                        pass
                except:
                    pass
    else:
        # att_name = input("Input Class Name: ")
        article_url_extract = doc.find_all(tag_name, {'class': att_name})
        for tag in article_url_extract:
            # print(tag)
            for item in tag.find_all('a', attrs={'href': re.compile("^https://")}):
                try:
                    condition_true_url = (re.search(url_id_extract, item.get('href')).group() == url_id_extract)
                    article_url_extract = re.search(url_id_extract, item.get('href')).group()
                    # print(article_url_extract)
                    if (len(item.get('href')) - len(article_url_extract)) > 50:
                        print(item.get('href'))
                    else:
                        pass
                except:
                    pass
    return
# news_article_scrapper()
