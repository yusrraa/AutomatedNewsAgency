from Scrapper import *
from Sanitization import *

def scrap():
    obj = Scrapper()
    print(obj.Scrape_news())

@scrap
def func():
    obj2 = Sanitisation()
    obj2.summarise()


