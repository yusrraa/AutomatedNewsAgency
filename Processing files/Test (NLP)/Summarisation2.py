import re
import nltk
import math
import heapq
from datetime import date
import pymysql

def summ():
    connection = pymysql.connect(host="localhost", user="root", passwd="newsagn", database="newsagn")
    cursor = connection.cursor()
    cursor.execute("select unprocessed_news_description from unprocesssed_scrape_data")
    descp = cursor.fetchall()
    file2 = open(r"C:\Users\Khawaja Masood Ahmed\Desktop\Test\Summarisation2.txt", "w+")
    for x in descp:
        text = ''.join(x)
        text = text.lower()
        cleantext = re.sub("[^a-zA-Z]", ' ', text)
        cleantext = re.sub("\s+", ' ', cleantext)
        sen_lst = nltk.sent_tokenize(text)
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
        for sentence in sen_lst:
            for word in nltk.word_tokenize(sentence):
                if word in word_frequencies:
                    if sentence not in word_frequencies:
                        sentence_prob[sentence] = (math.log(word_frequencies[word]) - math.log(len(text.split(' '))))
                    else:
                        sentence_prob[sentence] += (math.log(word_frequencies[word]) - math.log(len(text.split(' '))))

        len_Sen_lst = len(sen_lst)
        len_Sen_lst = math.ceil(len_Sen_lst * 0.6)
        summary = heapq.nlargest(len_Sen_lst, sentence_prob, key=sentence_prob.get)
        summ = " ".join(summary)
        file2.writelines(x)
        file2.write("\n")
        file2.writelines(summ)
        file2.write("\n\n\n")

    file2.close()
summ()

