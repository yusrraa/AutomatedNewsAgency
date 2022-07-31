from bs4 import BeautifulSoup
from selenium import webdriver


def image_scrapper(url, tag_name, scrape_by, att_name):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(executable_path="F:/Program Files (x86)/chromedriver.exe", options=options)
    # url = input("Enter Url: ")
    driver.get(url)
    # time.sleep(5)
    doc = BeautifulSoup(driver.page_source, "html.parser")
    # driver.quit()
    # all_tags = set([tag.name for tag in doc.find_all()])
    # print(all_tags)
    # tag_name = input("Select Tag name: ")
    # scrape_by = int(input("Enter \n(1)To Scrape By ID \n(2)To SCrape BY Class: "))
    if scrape_by == "id":
        # att_name = input("Enter id name: ")
        li = doc.find(tag_name, {'id': att_name})
        for descendant in li.descendants:
            if descendant.name == "img":
                return descendant['src']
    else:
        # att_name = input("Enter class name: ")
        li = doc.find(tag_name, {'class': att_name})
        for descendant in li.descendants:
            if descendant.name == "img":
                return descendant['src']
# image_scrapper()
