import re
import nltk
import math
import heapq


text = "China enforced a lockdown on over 18 million residents living in the Southern part of Shenzhen till at least March 20 on Sunday. China pursued a zero-covid policy due to which multiple cities were locked down. The omicron variant, however, made it very difficult for the country to continue with this approach. On Sunday, China reported twice the number of new cases from the day before, the total reaching 3,400. This makes it the worst outbreak in two years." \
       "Currently, the subways and trains in Shenzhen have stopped operating and the citizens have been instructed to limit their travel. "

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

#tot_words = len(cleantext)
print(word_frequencies)
sentence_score = {}
for sentence in sentence_list:
    freq = 0
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies:
            word_score = math.log(word_frequencies[word])
            print(word_score)
            freq = freq + word_score

    len_sen = len(sentence.split(' '))
    print(sentence)
    print(freq)
    print(len_sen)
    print("\n")
    sentence_score[sentence] = freq/len_sen

print("\n\n")
print(sentence_score)

len_Sen_lst = len(sentence_list)
len_Sen_lst = math.ceil(len_Sen_lst * 0.6)
summary = heapq.nlargest(len_Sen_lst, sentence_score, key=sentence_score.get)

summ = " ".join(summary)
print("\n",summ)






