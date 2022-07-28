from Scrapper import Scrapper
from Sanitization import Sanitization

def cronjob():
    scrapper = Scrapper()
    sanitization = Sanitization()
    scrapper.Scrape_news()
    sanitization.summarise()
    print("Chal para")

cronjob()


