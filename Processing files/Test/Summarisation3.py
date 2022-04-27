import re
import nltk
from sklearn.cluster import KMeans
from gensim.models import Word2Vec
from scipy.spatial import distance
import math
import pymysql

def summ():
    connection = pymysql.connect(host="localhost", user="root", passwd="newsagn", database="newsagn")
    cursor = connection.cursor()
    cursor.execute("select unprocessed_news_description from unprocesssed_scrape_data")
    descp = cursor.fetchall()
    file2 = open(r"C:\Users\Khawaja Masood Ahmed\Desktop\Test\Summarisation3.txt", "w+")
    for x in descp:
        text = ''.join(x)
        sentence = nltk.sent_tokenize(text)
        corpus = []
        stopwords = nltk.corpus.stopwords.words('english')

        for i in range(len(sentence)):
            sen = re.sub('[^a-zA-Z]', " ", sentence[i])
            sen = sen.lower()
            sen = sen.split()
            sen = ' '.join([i for i in sen if i not in stopwords])
            corpus.append(sen)

        print(sentence)
        print(corpus)

        all_words = [i.split() for i in corpus]
        print(all_words)''
        model = Word2Vec(all_words, min_count=1, size=300)

        sent_vector = []
        for i in corpus:
            plus = 0
            for j in i.split():
                plus += model.wv[j]  # Adds all the vectors of the words present in a single sentence
            plus = plus / len(i.split())

            sent_vector.append(plus)

        # print(sent_vector)

        n_clusters = 3
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

        print(my_dict)
        print(my_list)
        print("\n\n\n")
        for i in sorted(my_list):
            print(sentence[i])



        summ= " "
        for i in sorted(my_list):
            summ = " ".join(sentence[i])


        file2.writelines(x)
        file2.write("\n")
        file2.writelines(summ)
        file2.write("\n\n\n")

    file2.close()
summ()

