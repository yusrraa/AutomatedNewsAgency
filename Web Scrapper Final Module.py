from bs4 import BeautifulSoup
import requests

def scrapper():
    try:
        Data_file = open("Data_Scrape_File.txt", "w+")
        url = str(input("Enter URL: "))
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
    except:
        print("invalid Input")

print(scrapper())