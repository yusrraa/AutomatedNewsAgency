from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# initializing driver
options = Options()
options.headless = True
s = Service("F:/Program Files (x86)/chromedriver.exe")
driver = webdriver.Chrome(service=s,options=options)


def tags_scrapper(domain_url):
    extras=["body","header","html","footer"]
    driver.get(domain_url)
    #time.sleep(5)
    doc = BeautifulSoup(driver.page_source, "html.parser")
    remove_tag = [ "script", "noscript","input","title","g","svg","style","link"]
    for sel_tag in remove_tag:
        for scr in doc.find_all(sel_tag):
            scr.decompose()
    driver.quit()
    all_tags = set([tag.name for tag in doc.find_all()])
    for extra in all_tags:
        if extra in extras:
            all_tags.remove(extra)
    return all_tags

print(tags_scrapper("https://www.geo.tv/latest-news"))