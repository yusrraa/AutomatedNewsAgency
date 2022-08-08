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
    file2 = open(r"C:\Users\Khawaja Masood Ahmed\Desktop\Test\Summarisation.txt", "w+")
    for x in descp:
        text = ''.join(x)
        print(text)
        text = text.lower()
        cleantext = re.sub("[^a-zA-Z]", ' ', text)
        cleantext = re.sub("\s+", ' ', cleantext)
        stopwords = nltk.corpus.stopwords.words('english')
        sentence_list = nltk.sent_tokenize(text)
        word_frequencies = {}
        for word in nltk.word_tokenize(cleantext):
            if word not in stopwords:
                if word not in word_frequencies:
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

        # tot_words = len(cleantext)
        sentence_score = {}
        for sentence in sentence_list:
            freq = 0
            for word in nltk.word_tokenize(sentence):
                if word in word_frequencies:
                    word_score = math.log(word_frequencies[word])
                    freq = freq + word_score

            len_sen = len(sentence.split(' '))
            sentence_score[sentence] = freq / len_sen

        len_Sen_lst = len(sentence_list)
        len_Sen_lst = math.ceil(len_Sen_lst * 0.6)
        summary = heapq.nlargest(len_Sen_lst, sentence_score, key=sentence_score.get)
        summ = " ".join(summary)

        file2.writelines(x)
        file2.write("\n")
        file2.writelines(summ)
        file2.write("\n\n\n")

    file2.close()


summ()

