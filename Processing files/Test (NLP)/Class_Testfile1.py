import re
import nltk
import math
import heapq
import pymysql
from datetime import date


class Sanitisation:
    def __init__(self):
        self.t_date = date.today()

    def summarise(self):
        self.t_date = self.t_date.strftime("%d/%m/%Y")
        connection = pymysql.connect(host="localhost", user="root", passwd="newsagn", database="newsagn")
        cursor = connection.cursor()
        cursor.execute("select id, unprocessed_news_topic, unprocessed_news_description, image_href, scrape_date_stamp,"
                       " scrape_time_stamp  from unprocesssed_scrape_data where scrape_date_stamp <> '%s'" %self.t_date)
        unprcs_data = cursor.fetchall()
        for x in unprcs_data:
            art_id = x[0]
            art_top = x[1]
            art_news = x[2]
            art_img = x[3]
            art_date = x[4]
            art_time = x[5]
            text = art_news.lower()
            cleantext = re.sub("[^a-zA-Z]", ' ', text)
            cleantext = re.sub("\s+", ' ', cleantext)
            stopwords = nltk.corpus.stopwords.words('english')
            word_frequencies = {}
            for word in nltk.word_tokenize(cleantext):
                if word not in stopwords:
                    if word not in word_frequencies:
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1


            tot_words = len(text.split(' '))
            tot_words_log = math.log(tot_words)

            sentence_prob = {}
            sentence_scores = {}
            sen_lst = nltk.sent_tokenize(text)
            for sentence in sen_lst:
                for word in nltk.word_tokenize(sentence):
                    if word in word_frequencies:
                        if sentence not in word_frequencies:
                            sentence_prob[sentence] = (math.log(word_frequencies[word]) - math.log(len(text.split(' '))))
                        else:
                            sentence_prob[sentence] += (math.log(word_frequencies[word]) - math.log(len(text.split(' '))))

            len_sen_lst = len(sen_lst)
            len_sen_lst = math.ceil(len_sen_lst * 0.6)
            summary = heapq.nlargest(len_sen_lst, sentence_prob, key=sentence_prob.get)
            summ = " ".join(summary)

            cursor.execute("Insert into processsed_scrape_data (article_id,processed_news_topic,processed_news_description,image_href,scrape_date_stamp,scrape_time_stamp) "
                           "values (%s,%s,%s,%s,%s,%s)", (art_id, art_top, summ, art_img, art_date, art_time))
            connection.commit()

        return




