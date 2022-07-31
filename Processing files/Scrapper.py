# importing libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime, date
import time
import re
import pymysql


class ArticleUrlConfig:

    def get_article_url_config(self,url_id):
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                     database="automated_news_broadcast")
        cursor = connection.cursor()
        # Extracting all article url configuration details from database against url
        cursor.execute(
            "Select tag_name,scrape_type,attribute_name from article_url_configuration where domain_url_id = '%s'"
            % url_id)
        article_url_config_lst = cursor.fetchall()  # store the extracted data into variable
        connection.close()
        return article_url_config_lst


class ImgConfig:
    def get_article_img_config(self,url_id):
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                     database="automated_news_broadcast")
        cursor = connection.cursor()
        # Extracting all article url configuration details from database against url
        cursor.execute(
            "Select tag_name,scrape_type,attribute_name from article_img_configuration where domain_url_id = '%s'" % url_id)
        article_img_config_lst = cursor.fetchall()  # store the extracted data into variable
        connection.close()
        return article_img_config_lst


class PublishConfig:
    def get_article_publish_date_config(self,url_id):
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                     database="automated_news_broadcast")
        cursor = connection.cursor()
        # Extracting all article url configuration details from database against url
        cursor.execute(
            "Select tag_name,scrape_type,attribute_name from article_publish_date_configuration where domain_url_id = '%s'"
            % url_id)
        article_pub_date_config_lst = cursor.fetchall()  # store the extracted data into variable
        connection.close()
        return article_pub_date_config_lst


class HeadlineConfig:
    def get_article_topic_head_config(self,url_id):
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                     database="automated_news_broadcast")
        cursor = connection.cursor()
        # Extracting all article url configuration details from database against url
        cursor.execute(
            "Select parent_tag_name,child_tag_name,scrape_type,attribute_name from article_topic_headline_configuration "
            "where domain_url_id = '%s'"
            % url_id)
        article_head_config_lst = cursor.fetchall()  # store the extracted data into variable
        connection.close()
        return article_head_config_lst


class TextConfig:

    def get_article_text_config(self,url_id):
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                     database="automated_news_broadcast")
        cursor = connection.cursor()
        # Extracting all article url configuration details from database against url
        cursor.execute(
            "Select tag_name,scrape_type,attribute_name from article_text_configuration where domain_url_id = '%s'" %
            url_id)
        article_text_config_lst = cursor.fetchall()  # store the extracted data into variable
        connection.close()
        return article_text_config_lst


class Url(ArticleUrlConfig):
    def get_domain_url(self):
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                     database="automated_news_broadcast")
        cursor = connection.cursor()
        # Extracting all url and their ids from database
        cursor.execute("Select id,url,is_active from domain_url where is_active = '%s'" % 1)
        url_detail_lst = cursor.fetchall()  # store the extracted data into variable
        connection.close()
        return url_detail_lst

    def get_article_url(self ,url_id, domain_url):
        # Following Section Scrape all the article urls from domain url and return lst
        article_url_extracted_lst = []
        article_url_config_lst = ArticleUrlConfig().get_article_url_config(url_id)  # gets all details of article url config
        options = webdriver.ChromeOptions()
        options.headless = True
        s = Service("F:/Program Files (x86)/chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=options)
        driver.get(domain_url)
        time.sleep(5)
        doc = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
        url_domain_id = re.search('/(.+?)/', domain_url).group(0)
        url_id_extract = "https:" + url_domain_id
        if article_url_config_lst[0][1] == "id":
            article_url_extract = doc.find_all(article_url_config_lst[0][0], {'id': article_url_config_lst[0][2]})
            for tag in article_url_extract:
                # print(tag)
                for item in tag.find_all('a', attrs={'href': re.compile("^https://")}):
                    try:
                        condition_true_url = (re.search(url_id_extract, item.get('href')).group() == url_id_extract)
                        article_url_extract = re.search(url_id_extract, item.get('href')).group()
                        if (len(item.get('href')) - len(article_url_extract)) > 50:
                            # database connection
                            connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                                         database="automated_news_broadcast")
                            cursor = connection.cursor()
                            # Extracting all article url configuration details from database against url
                            cursor.execute(
                                "select article_url from article where article_url = '%s'" % (item.get('href')))
                            redundant_article_url = cursor.fetchall()
                            connection.close()
                            if len(redundant_article_url) == 0:
                                print(item.get('href'))
                                article_url_extracted_lst.append(item.get('href'))
                                # database connection
                                connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                                             database="automated_news_broadcast")
                                cur = connection.cursor()
                                # inserting article url into database
                                cur.execute("Insert into article (url_id,article_url) values (%s,%s)",
                                            (url_id, item.get('href')))
                                connection.commit()
                            else:
                                pass

                        else:
                            pass
                    except:
                        pass
        else:
            article_url_extract = doc.find_all(article_url_config_lst[0][0], {'class': article_url_config_lst[0][2]})
            for tag in article_url_extract:
                # print(tag)
                for item in tag.find_all('a', attrs={'href': re.compile("^https://")}):
                    try:
                        condition_true_url = (re.search(url_id_extract, item.get('href')).group() == url_id_extract)
                        article_url_extract = re.search(url_id_extract, item.get('href')).group()
                        # print(article_url_extract)
                        if (len(item.get('href')) - len(article_url_extract)) > 50:
                            # database connection
                            connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                                         database="automated_news_broadcast")
                            cursor = connection.cursor()
                            # Extracting all article url configuration details from database against url
                            cursor.execute("select id from article where article_url = '%s'" % (item.get('href')))
                            redundant_article_url = cursor.fetchall()
                            connection.close()
                            if len(redundant_article_url) == 0:
                                print(item.get('href'))
                                article_url_extracted_lst.append(item.get('href'))
                                # database connection
                                connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                                             database="automated_news_broadcast")
                                cur = connection.cursor()
                                # inserting article url into database
                                cur.execute("Insert into article (url_id,article_url) values (%s,%s)",
                                            (url_id, item.get('href')))
                                connection.commit()
                            else:
                                pass

                        else:
                            pass
                    except:
                        pass
        return article_url_extracted_lst


class Scrapper(Url, ArticleUrlConfig, ImgConfig, PublishConfig, HeadlineConfig, TextConfig):
    def Scrape_news(self):
        merged_data = ""
        url_details_lst = Url().get_domain_url()  # Get all domain url table details  #line 1
        for url_id in range(len(url_details_lst)):  # get all url one by one #line 2
            article_text_config_details = TextConfig().get_article_text_config(url_details_lst[url_id][0])  # get all article text config details #line 3
            article_url_extracted_lst = Url().get_article_url(url_details_lst[url_id][0],url_details_lst[url_id][1])  # get all articles url in lst #line 4
            article_topic_head_lst = HeadlineConfig().get_article_topic_head_config(url_details_lst[url_id][0])  # get news headline config details #line 5
            article_pub_date_lst = PublishConfig().get_article_publish_date_config(url_details_lst[url_id][0])  # get publish date config details #line 6
            article_img_config_lst = ImgConfig().get_article_img_config(url_details_lst[url_id][0])  # get news image config details #line 7
            for article_url in article_url_extracted_lst:  # get all article url from domain url one by one #line 8
                options = Options()
                options.headless = True
                s = Service("F:/Program Files (x86)/chromedriver.exe")
                driver = webdriver.Chrome(service=s, options=options)
                driver.get(article_url)
                time.sleep(5)
                doc = BeautifulSoup(driver.page_source, "html.parser")
                remove_tag = ['header', 'script', 'noscript', 'footer', "button", "input", "style"] #line 9
                for sel_tag in remove_tag:
                    for scr in doc.find_all(sel_tag): #line 10
                        scr.decompose()
                driver.quit()
                try:
                    # Following Section Scrape all the text description from url
                    for article_text_config in range(len(article_text_config_details)): #line 11
                        if article_text_config_details[article_text_config][1] == "id": #line 12
                            page_text = doc.find_all(article_text_config_details[article_text_config][0],
                                                     id=article_text_config_details[article_text_config][2]) #line 13
                            for scrp in page_text:
                                content = scrp.contents
                                for grab in content:
                                    if str(grab.string) == "None" or str(grab.string) == "" or str(grab.string) == "\n":
                                        pass
                                    else:
                                        merged_data = merged_data + str(grab.string) + "\n"
                        else:
                            page_text = doc.find_all(article_text_config_details[article_text_config][0],
                                                     class_=article_text_config_details[article_text_config][2]) #line 14
                            for scrp in page_text:
                                content = scrp.contents
                                for grab in content:
                                    if str(grab.string) == "None" or str(grab.string) is None or str(
                                            grab.string) == "\n":
                                        pass
                                    else:
                                        merged_data = merged_data + str(grab.string) + "\n"
                    print("All Data Together: ", merged_data) #line 15

                    # Following Section Scrape all the text headline from url
                    article_headline = ""
                    try:
                        if article_topic_head_lst[0][2] == "id":
                            article_topic_headline = doc.find(article_topic_head_lst[0][0],
                                                              {'id': article_topic_head_lst[0][3]})
                            for item in article_topic_headline.find(article_topic_head_lst[0][1]): #line 16
                                if str(item.string) is None or str(item.string) == "None" or str(item.string) == "\n":
                                    pass
                                else:
                                    article_headline += str(item.string)
                                    print("Article Headline: ", item.string)
                        else:
                            article_topic_headline = doc.find(article_topic_head_lst[0][0],
                                                              {'class': article_topic_head_lst[0][3]}) #line 17
                            for item in article_topic_headline.find(article_topic_head_lst[0][1]):
                                if str(item.string) is None or str(item.string) == "None" or str(item.string) == "\n":
                                    pass
                                else:
                                    article_headline += str(item.string)
                                    print("Article Headline: ", item.string)
                    except AttributeError: #line 18
                        article_headline = "None"
                    except RuntimeError: #line 19
                        article_headline = "None"
                    except DeprecationWarning: #line 20
                        article_headline = "None"

                    # Following Section Scrape all the text publish date from url
                    article_date = ""
                    try:
                        if article_pub_date_lst[0][1] == "id":
                            time_date_publish = doc.find_all(article_pub_date_lst[0][0],
                                                             {'id': article_pub_date_lst[0][2]}) # line 21
                            article_date += str(time_date_publish[0].text)
                            print(time_date_publish[0].text)
                        elif article_pub_date_lst[0][1] == "class":
                            time_date_publish = doc.find_all(article_pub_date_lst[0][0],
                                                             {'class': article_pub_date_lst[0][2]}) # line 22
                            article_date += str(time_date_publish[0].text)
                            print(time_date_publish[0].text)
                        else:
                            article_date += "None"
                            print("None")
                    except AttributeError: # line 23
                        article_date = "None"
                    except RuntimeError:
                        article_date = "None"
                    except DeprecationWarning:
                        article_date = "None"

                    # Following Section Scrape article image from url
                    article_img_url = ""
                    try:
                        if article_img_config_lst[0][1] == "id":
                            li = doc.find(article_img_config_lst[0][0], {'id': article_img_config_lst[0][2]}) # line 24
                            for descendant in li.descendants:
                                if descendant.name == "img":
                                    article_img_url += str(descendant['src'])
                                    print(descendant['src'])
                        elif article_img_config_lst[0][1] == "class":
                            li = doc.find(article_img_config_lst[0][0], {'class': article_img_config_lst[0][2]}) # line 25
                            for descendant in li.descendants: # line 26
                                if descendant.name == "img": # liine 27
                                    article_img_url += str(descendant['src'])
                                    print(descendant['src']) # line 28
                        else:
                            article_img_url += "None"
                            print("None") # line 29
                    except AttributeError: # line 30
                        article_img_url = "None"
                    except RuntimeError:
                        article_img_url = "None"
                    except DeprecationWarning:
                        article_img_url = "None"
                    # database connection
                    connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                                 database="automated_news_broadcast") # line 31
                    cursor = connection.cursor()
                    # Extracting all article url configuration details from database against url
                    cursor.execute("select id from article where article_url = '%s'" % article_url) # line 32
                    article_url_id = cursor.fetchall()
                    connection.close()
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    today = date.today()
                    current_date = today.strftime("%d/%m/%Y")  # dd/mm/YY
                    # database connection
                    connection = pymysql.connect(host="localhost", user="root", passwd="q1w2e3rty12345",
                                                 database="automated_news_broadcast")
                    cur = connection.cursor()
                    if article_headline != "None" or article_headline is not None:
                        # inserting article url into database
                        cur.execute(
                            "Insert into unprocesssed_scrape_data (article_id,unprocessed_news_topic,unprocessed_news_description,publication_date,image_href,scrape_date_stamp,scrape_time_stamp) "
                            "values (%s,%s,%s,%s,%s,%s,%s)",
                            (article_url_id[0][0], article_headline, merged_data, article_date, article_img_url,
                             current_date, current_time)) # line 33
                        connection.commit()
                        merged_data = ""
                    else:
                        pass
                except:
                    pass
        return


object = Scrapper()
print(object.Scrape_news())

