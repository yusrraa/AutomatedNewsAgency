from bs4 import BeautifulSoup
import requests
import re

def scrapper():
    try:
        domain_url = str(input("Enter URL: "))
        user_file = str(input("Enter File Name: "))
        Data_file = open(user_file + ".txt", "w+", encoding="utf-8")
        domain_result = requests.get(domain_url).text
        domain_doc = BeautifulSoup(domain_result, "html.parser")
        domain_body = domain_doc.body
        remove_tag = ['header', 'script', 'noscript', 'img', 'footer', 'figure', "button", "input", "style"]
        for sel_tag in remove_tag:
            for scr in domain_body.find_all(sel_tag):
                scr.decompose()
        for anker_tag in domain_body.find_all('a', attrs={'href': re.compile("^https://")}):
            print("Href of tag: ", anker_tag.get('href'))
            url = str(anker_tag.get('href'))
            result = requests.get(url).text
            doc = BeautifulSoup(result, "html.parser")
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
                    for grab in content:
                        if grab.name != None:
                            if grab.string != None and grab.string != "\n":
                                print("Tag Name: ", grab.name)
                                print("Tag String",grab.string)
                                print("\n")
                                Data_file.write("Tag Name: %s \nTag String: %s \n" % (grab.name,grab.string))
                            else:
                                pass
                        else:
                            pass
            Data_file.write("New Anker Tag URL Data Scrape")
        Data_file.close()
    except:
        print("Invalid Input")

print(scrapper())
