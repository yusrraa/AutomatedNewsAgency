import re
import nltk
import heapq


text = "China enforced a lockdown on over 18 million residents living in the Southern part of Shenzhen till at least March 20 on Sunday. China pursued a zero-covid policy due to which multiple cities were locked down. The omicron variant, however, made it very difficult for the country to continue with this approach. On Sunday, China reported twice the number of new cases from the day before, the total reaching 3,400. This makes it the worst outbreak in two years." \
       "Currently, the subways and trains in Shenzhen have stopped operating and the citizens have been instructed to limit their travel. "

print(text)

text = text.lower()

cleantext = re.sub("[^a-zA-Z]", ' ', text)
cleantext = re.sub("\s+", ' ', cleantext)

print(cleantext)


sen_lst = nltk.sent_tokenize(text)

print(sen_lst)

stopwords = nltk.corpus.stopwords.words('english')
print(stopwords)
word_frequencies = {}
for word in nltk.word_tokenize(cleantext):
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

print(word_frequencies)

maximum_frequency = max(word_frequencies.values())

print(maximum_frequency, "\n\n")
for word in word_frequencies:
    word_frequencies[word] = word_frequencies[word] / maximum_frequency

sentence_scores = {}

for sentence in sen_lst:
    for word in nltk.word_tokenize(sentence):
        print("length", len(sentence.split(' ')))
        if word in word_frequencies and len(sentence.split(' ')) < 30:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]

print(word_frequencies)
print(sentence_scores)

summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

print(" ".join(summary))