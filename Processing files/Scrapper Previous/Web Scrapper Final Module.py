from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
#from webdriver_manager.chrome import ChromeDriverManager
import requests

def scrapper():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe", options=options)
    url = str(input("Enter URL: "))
    user_file = str(input("Enter File Name: "))
    Data_file = open(user_file + ".txt", "w+", encoding="utf-8")
    driver.get(url)
    #driver.get("https://www.proptiger.com/all-projects")
    time.sleep(5)
    doc = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    body = doc.body
    remove_tag = ['header', 'script', 'noscript', 'img', 'footer', 'figure', "button", "input","style"]
    for sel_tag in remove_tag:
        for scr in body.find_all(sel_tag):
            scr.decompose()
    all_tags = set([tag.name for tag in body.find_all()])
    print(all_tags)
    for single_tag in list(all_tags):
        for scrp in body.find_all(single_tag):
            content = scrp.contents
            for grap in content:
                if grap.name != None:
                    if grap.string != None and grap.string != "\n":
                        print("Tag Name: ", grap.name)
                        print("Tag String",grap.string)
                        print("\n")
                        Data_file.write("Tag Name: %s \nTag String: %s \n" % (grap.name,grap.string))
                    else:
                        pass
                else:
                    pass
    Data_file.close()

print(scrapper())