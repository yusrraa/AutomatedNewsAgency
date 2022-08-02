import re
import nltk
from sklearn.cluster import KMeans
from gensim.models import Word2Vec
from scipy.spatial import distance


text = "China enforced a lockdown on over 18 million residents living in the Southern part of Shenzhen till at least March 20 on Sunday. China pursued a zero-covid policy due to which multiple cities were locked down. The omicron variant, however, made it very difficult for the country to continue with this approach. On Sunday, China reported twice the number of new cases from the day before, the total reaching 3,400. This makes it the worst outbreak in two years." \
       "Currently, the subways and trains in Shenzhen have stopped operating and the citizens have been instructed to limit their travel. "

print(text)
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
print(all_words)
model = Word2Vec(all_words, min_count=1,size= 300)

sent_vector = []
for i in corpus:
       plus = 0
       for j in i.split():
              plus += model.wv[j]  #Adds all the vectors of the words present in a single sentence
       plus = plus / len(i.split())

       sent_vector.append(plus)

#print(sent_vector)

n_clusters = 3
kmeans = KMeans(n_clusters, init = 'k-means++', random_state = 42)
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
x = ""
for i in sorted(my_list):
    y = sentence[i]
    x = x+y

print(x)
print("\n\n\n")
for i in sorted(my_list):
    print(sentence[i])

