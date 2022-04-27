import re
import nltk
import math
import heapq


text = "China enforced a lockdown on over 18 million residents living in the Southern part of Shenzhen till at least March 20 on Sunday. China pursued a zero-covid policy due to which multiple cities were locked down. The omicron variant, however, made it very difficult for the country to continue with this approach. On Sunday, China reported twice the number of new cases from the day before, the total reaching 3,400. This makes it the worst outbreak in two years." \
       "Currently, the subways and trains in Shenzhen have stopped operating and the citizens have been instructed to limit their travel. "

print(text)

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

print(word_frequencies)

tot_words = len(text.split(' '))
tot_words_log = math.log(tot_words)
#for word in word_frequencies:
#    word_frequencies[word] = word_frequencies[word]/tot_words

print("\n")
#print(word_frequencies)

sentence_scores = {}
sen_lst = nltk.sent_tokenize(text)
for sentence in sen_lst:
    freq = 0
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies:
            word_freq = math.log(word_frequencies[word])
            tot_word_freq = word_freq- tot_words_log
            freq += tot_word_freq
    sentence_scores[sentence] = freq


print(sentence_scores)

sentence_prob={}

for sentence in sen_lst:
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies:
            if sentence not in word_frequencies:
                sentence_prob[sentence] = (math.log(word_frequencies[word]) - math.log(len(text.split(' '))))
            else:
                sentence_prob[sentence] += (math.log(word_frequencies[word]) - math.log(len(text.split(' '))))


print("\n", sentence_prob)


#sort_orders = sorted(sentence_prob.items(), key=lambda x: x[1], reverse=True)
#print(sort_orders)

#for i in sort_orders:
#    print(i[0], i[1])


print("\n\n\n")

len_Sen_lst = len(sen_lst)
len_Sen_lst = math.ceil(len_Sen_lst * 0.6)
summary = heapq.nlargest(len_Sen_lst, sentence_prob, key=sentence_prob.get)
print(" ".join(summary))