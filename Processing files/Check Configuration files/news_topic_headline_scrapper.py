from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


def news_topic_headline_scraper(url, parent_tag_name, child_tag_name, scrape_by, att_name):
    options = webdriver.ChromeOptions()
    options.headless = True
    s = Service("F:/Program Files (x86)/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    # url = input("Enter Url: ")
    driver.get(url)
    time.sleep(5)
    doc = BeautifulSoup(driver.page_source, "html.parser")
    # driver.quit()
    # all_tags = set([tag.name for tag in doc.find_all()])
    # print(all_tags)
    # extract Date
    # scrape_by = int(input("Enter \n(1)To Scrape By ID \n(2)To SCrape BY Class: "))
    article_headline = ""
    if scrape_by == "id":
        # parent_tag_name = input("Select Tag name: ")
        # att_name = input("Enter id name: ")
        # child_tag_name = input("Enter child tag name: ")
        article_topic_headline = doc.find(parent_tag_name, {'id': att_name})
        for item in article_topic_headline.find(child_tag_name):
            if str(item.string) is None or str(item.string) == "None" or str(item.string) == "\n":
                pass
            else:
                article_headline += str(item.string)
                return item.string

    else:
        # head_tag_name = input("Select Tag name: ")
        # head_class_name = input("Enter class name: ")
        # head_child_tag_name = input("Enter child tag name: ")
        article_topic_headline = doc.find(parent_tag_name, {'class': att_name})
        for item in article_topic_headline.find(child_tag_name):
            if str(item.string) is None or str(item.string) == "None" or str(item.string) == "\n":
                pass
            else:
                article_headline += str(item.string)
                return item.string


# news_topic_headline_scraper()
