from Scrapper import *
from Sanitisation import *


obj = Scrapper()
print(obj.Scrape_news())

obj2 = Sanitisation()
obj2.summarise()
