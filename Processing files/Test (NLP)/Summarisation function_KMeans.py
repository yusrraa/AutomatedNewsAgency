import re
import nltk
from sklearn.cluster import KMeans
from gensim.models import Word2Vec
from scipy.spatial import distance
import math
import heapq
from datetime import date
import pymysql

def summ():
    connection = pymysql.connect(host="localhost", user="root", passwd="newsagn", database="newsagn")
    cursor = connection.cursor()
    cursor.execute("select unprocessed_news_description from unprocesssed_scrape_data")
    descp = cursor.fetchall()
    file3 = open(r"C:\Users\Khawaja Masood Ahmed\Desktop\UIT\FYP\Processing files\Test\Summarisation_KMeans.txt", "w+")
    for news in descp:
        for text in news:
            sentence = nltk.sent_tokenize(text)
            len_sen_lst = len(sentence)
            len_sen_lst = math.ceil(len_sen_lst * 0.6)
            corpus = []
            stopwords = nltk.corpus.stopwords.words('english')

            for i in range(len(sentence)):
                sen = re.sub('[^a-zA-Z]', " ", sentence[i])
                sen = sen.lower()
                sen = sen.split()
                sen = ' '.join([i for i in sen if i not in stopwords])
                corpus.append(sen)

            all_words = [i.split() for i in corpus]
            words = [x for x in all_words if x != []]

            if words == []:
                break
            model = Word2Vec(words, min_count=1, size=300)
            sent_vector = []

            for i in corpus:
                if i == "":
                    break
                plus = 0
                for j in i.split():
                    plus += model.wv[j]  # Adds all the vectors of the words present in a single sentence
                plus = plus / len(i.split())

                sent_vector.append(plus)

            n_clusters = len_sen_lst
            kmeans = KMeans(n_clusters, init='k-means++', random_state=42)
            y_kmeans = kmeans.fit_predict(sent_vector)

            my_list = []
            for i in range(n_clusters):
                my_dict = {}

                for j in range(len(y_kmeans)):

                    if y_kmeans[j] == i:
                        my_dict[j] = distance.euclidean(kmeans.cluster_centers_[i], sent_vector[j])
                min_distance = min(my_dict.values())
                my_list.append(min(my_dict, key=my_dict.get))

            sum_news = ""
            for i in sorted(my_list):
                sen = sentence[i]
                sum_news = sum_news + sen

            file3.writelines(text)
            file3.write("\n")
            file3.writelines(sum_news)
            file3.write("\n\n\n")



print(summ())