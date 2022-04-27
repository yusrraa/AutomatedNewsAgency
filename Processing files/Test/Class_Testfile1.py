import re
import nltk
import math
import heapq
from datetime import date


class Sanitisation:
    def __init__(self, article_id):
        self.article_id = article_id

    def summarise(self):
        connection = pymysql.connect(host="localhost", user="root", passwd="newsagn", database="newsagn")
        cursor = connection.cursor()
        for art_id in self.article_id:
            cursor.execute("select publication_date from unprocesssed_scrape_data where article_id = '%s'" % art_id)
            date = cursor.fetchall()
            date_today = date.today()
            if date == date_today:
                cursor.execute("select unprocessed_news_description from unprocesssed_scrape_data where article_id = '%s'" % art_id)
                text = cursor.fetchall()
                print(text)
                text = text.lower()
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
                print(word_frequencies)

                tot_words = len(text.split(' '))
                tot_words_log = math.log(tot_words)

                print("\n")
                sentence_prob = {}
                sentence_scores = {}
                sen_lst = nltk.sent_tokenize(text)
                for sentence in sen_lst:
                    for word in nltk.word_tokenize(sentence):
                        if word in word_frequencies:
                            if sentence not in word_frequencies:
                                sentence_prob[sentence] = (
                                            math.log(word_frequencies[word]) - math.log(len(text.split(' '))))
                            else:
                                sentence_prob[sentence] += (
                                            math.log(word_frequencies[word]) - math.log(len(text.split(' '))))

                print("\n", sentence_prob)
                print("\n\n\n")

                len_sen_lst = len(sen_lst)
                len_sen_lst = math.ceil(len_sen_lst * 0.6)
                summary = heapq.nlargest(len_sen_lst, sentence_prob, key=sentence_prob.get)

                # print(" ".join(summary))
                # return summary
                # a list to be incorporated in the database




A = Sanitisation(1234)
print(A.summarise())


# list with conditions,
# date and time limit
