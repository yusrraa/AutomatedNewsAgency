from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


def news_data_scrapper(url, tag_name, scrape_by, att_name):
    options = webdriver.ChromeOptions()
    options.headless = True
    s = Service("F:/Program Files (x86)/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    # url = input("Enter Url: ")
    driver.get(url)
    time.sleep(2)
    doc = BeautifulSoup(driver.page_source, "html.parser")
    # driver.quit()
    remove_tag = ['header', 'script', 'noscript', 'img', 'footer', 'figure', "button", "input", "ul",
                  "style", "sup", "hr", "br", "iframe", "label", "nav", "form", "svg", 'meta',
                  'fieldset', "li", "ins", "style"]
    for sel_tag in remove_tag:
        for scr in doc.find_all(sel_tag):
            scr.decompose()
    # all_tags = set([tag.name for tag in doc.find_all()])
    # print(all_tags)
    # tag_name = input("Select Tag name: ")
    # scrape_by = int(input("Enter \n(1)To Scrape By ID \n(2)To SCrape BY Class: "))
    if scrape_by == "id":
        # id_name = input("Enter id name: ")
        page_text = doc.find_all(tag_name, id=att_name)
        for scrp in page_text:
            content = scrp.contents
            for grab in content:
                if str(grab.string) == "None" or str(grab.string) is None or str(grab.string) == "\n":
                    pass
                else:
                    print(grab.string)
    else:
        # class_name = input("Enter class name: ")
        page_text = doc.find_all(tag_name, class_=att_name)
        for scrp in page_text:
            content = scrp.contents
            for grab in content:
                if str(grab.string) == "None" or str(grab.string) is None or str(grab.string) == "\n":
                    pass
                else:
                    print(grab.string)
    return
# news_data_scrapper()

