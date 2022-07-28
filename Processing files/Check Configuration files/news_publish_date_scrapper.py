from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def publish_date_scrapper(url, tag_name, att_name):
    options = webdriver.ChromeOptions()
    options.headless = True
    s = Service("F:/Program Files (x86)/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    # url = input("Enter Url: ")
    driver.get(url)
    # time.sleep(5)
    doc = BeautifulSoup(driver.page_source, "html.parser")
    # driver.quit()
    # all_tags = set([tag.name for tag in doc.find_all()])
    # print(all_tags)
    # #extract Date
    # publish_tag_name = input("Select Tag name: ")
    # att_name = input("Enter class name: ")
    try:
        time_date_publish = doc.find_all(tag_name, {'class': att_name})
        return time_date_publish[0].text
    except:
        return "None"

# publish_date_scrapper()
